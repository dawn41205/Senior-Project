"""
CKIP BERT 雙任務分類器：
  1. promise_status  — 只用 data 內文（禁止使用 promise_string，否則 Data Leakage）
  2. evidence_status — 拼接 promise_string + data（合法，因為 ES 需要比對承諾與內文）

訓練完成後會儲存到 bert_ps_model 和 bert_es_model
"""
import os, json, torch, warnings, re
import numpy as np
from collections import Counter
from datasets import Dataset
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments, Trainer, DataCollatorWithPadding
)
from sklearn.metrics import f1_score, classification_report

warnings.filterwarnings('ignore')

MODEL_ID = "ckiplab/bert-base-chinese"

TASKS = {
    "promise_status": {
        "labels": {"No": 0, "Yes": 1},
        "output_dir": "./bert_ps_checkpoints",
        "model_dir": "./bert_ps_model",
        "manual_weights": None,  # 用 balanced 公式
    },
    "evidence_status": {
        "labels": {"No": 0, "Yes": 1, "N/A": 2},
        "output_dir": "./bert_es_checkpoints",
        "model_dir": "./bert_es_model",
        # 手動加強 No 的權重到 8x（No 類別極度稀少，balanced 公式只給 ~2.7x 不夠）
        "manual_weights": {0: 8.0, 1: 0.5, 2: 1.8},
    },
}

def compute_metrics(eval_pred, id_to_label):
    preds = np.argmax(eval_pred.predictions, axis=1)
    labels = eval_pred.label_ids
    f1 = f1_score(labels, preds, average="macro", zero_division=0)
    for i, name in id_to_label.items():
        mask = (labels == i)
        if mask.sum() > 0:
            correct = (preds[mask] == i).sum()
            print(f"  {name:5s}: {correct}/{mask.sum()} = {correct/mask.sum():.1%}")
    return {"f1_macro": f1}

class WeightedTrainer(Trainer):
    """自訂 Trainer：在 CrossEntropyLoss 中套用 class_weight 以處理類別不平衡"""
    def __init__(self, class_weights=None, **kwargs):
        super().__init__(**kwargs)
        if class_weights is not None:
            self.class_weights = torch.tensor(class_weights, dtype=torch.float32)
        else:
            self.class_weights = None

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.logits
        if self.class_weights is not None:
            weight = self.class_weights.to(logits.device)
            loss_fn = torch.nn.CrossEntropyLoss(weight=weight)
        else:
            loss_fn = torch.nn.CrossEntropyLoss()
        loss = loss_fn(logits, labels)
        return (loss, outputs) if return_outputs else loss

def load_data(file_path, task_name, label_map):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    texts, labels = [], []
    for item in data:
        text = item.get("data", "")
        promise = item.get("promise_string", "")

        # ⚠️ 防外洩：PS 模型只看 data 內文
        # ES 模型可拼接 promise_string（需要對比承諾與執行狀況）
        if task_name != "promise_status" and promise:
            combined = f"承諾：{promise}\n\n報告內容：{text}"
        else:
            combined = text

        texts.append(combined)
        labels.append(label_map[item[task_name]])
    return Dataset.from_dict({"text": texts, "label": labels})

def train_task(task_name, config):
    label_map = config["labels"]
    id_to_label = {v: k for k, v in label_map.items()}
    n_classes = len(label_map)

    print(f"\n{'='*60}")
    print(f"  訓練 {task_name} — CKIP BERT")
    print(f"{'='*60}")

    train_ds = load_data("train_grouped.json", task_name, label_map)
    val_ds = load_data("val_grouped.json", task_name, label_map)

    # 計算 class_weight
    label_counts = Counter(train_ds["label"])
    total = sum(label_counts.values())

    if config["manual_weights"]:
        class_weights = [config["manual_weights"][i] for i in range(n_classes)]
        print("使用手動 class_weight:")
    else:
        class_weights = [total / (n_classes * label_counts[i]) for i in range(n_classes)]
        print("使用 balanced class_weight:")

    for i in range(n_classes):
        print(f"  {id_to_label[i]:5s}: {label_counts[i]:4d} 筆, weight = {class_weights[i]:.2f}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    def tokenize(examples):
        return tokenizer(examples["text"], truncation=True, max_length=512)

    tok_train = train_ds.map(tokenize, batched=True)
    tok_val = val_ds.map(tokenize, batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, num_labels=n_classes)

    training_args = TrainingArguments(
        output_dir=config["output_dir"],
        learning_rate=3e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=10,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,
        fp16=True,
        warmup_ratio=0.1,
        weight_decay=0.01,
        logging_steps=50,
        report_to="none",
        dataloader_num_workers=0,
    )

    trainer = WeightedTrainer(
        class_weights=class_weights,
        model=model,
        args=training_args,
        train_dataset=tok_train,
        eval_dataset=tok_val,
        processing_class=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
        compute_metrics=lambda ep: compute_metrics(ep, id_to_label),
    )

    # 檢查 checkpoint (支援斷點續訓)
    last_ckpt = None
    if os.path.exists(config["output_dir"]):
        ckpts = [d for d in os.listdir(config["output_dir"]) if d.startswith("checkpoint")]
        if ckpts:
            ckpts.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))
            last_ckpt = os.path.join(config["output_dir"], ckpts[-1])
            print(f"\n[恢復] 從 {last_ckpt} 繼續訓練")

    print("\n開始訓練...")
    trainer.train(resume_from_checkpoint=last_ckpt)

    # 儲存最佳模型
    print(f"\n儲存到 {config['model_dir']}...")
    trainer.save_model(config["model_dir"])
    tokenizer.save_pretrained(config["model_dir"])

    # 最終評估
    preds_output = trainer.predict(tok_val)
    preds = np.argmax(preds_output.predictions, axis=1)
    labels = preds_output.label_ids

    target_names = [id_to_label[i] for i in range(n_classes)]
    print(f"\n{'='*60}")
    print(f"  {task_name} 最終結果")
    print(f"{'='*60}")
    print(classification_report(labels, preds, target_names=target_names, digits=4))

    return f1_score(labels, preds, average="macro", zero_division=0)

def main():
    results = {}
    for task_name, config in TASKS.items():
        f1 = train_task(task_name, config)
        results[task_name] = f1

    print(f"\n{'='*60}")
    print(f"  所有任務完成！")
    print(f"{'='*60}")
    for task, f1 in results.items():
        print(f"  {task:25s}: F1 = {f1:.4f}")

if __name__ == "__main__":
    main()
