import argparse
import copy
import json
import os
import shutil
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from datasets import Dataset
from sklearn.metrics import classification_report, f1_score
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
)

from week13_fold_utils import split_train_internal_dev


MODEL_ID = "ckiplab/bert-base-chinese"

TASKS = {
    "promise_status": {
        "labels": {"No": 0, "Yes": 1},
        "id_to_label": {0: "No", 1: "Yes"},
        "epochs": 8,
        "manual_weights": None,
    },
    "evidence_status": {
        "labels": {"No": 0, "Yes": 1, "": 2, "N/A": 2},
        "id_to_label": {0: "No", 1: "Yes", 2: ""},
        "epochs": 8,
        "manual_weights": {0: 8.0, 1: 0.5, 2: 1.8},
    },
}


class WeightedTrainer(Trainer):
    def __init__(self, class_weights=None, focal_gamma=0.0, **kwargs):
        super().__init__(**kwargs)
        self.class_weights = (
            torch.tensor(class_weights, dtype=torch.float32)
            if class_weights is not None
            else None
        )
        self.focal_gamma = float(focal_gamma)

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.logits
        weights = self.class_weights.to(logits.device) if self.class_weights is not None else None
        if self.focal_gamma > 0:
            loss = focal_cross_entropy(logits, labels, class_weights=weights, gamma=self.focal_gamma)
        else:
            loss_fn = torch.nn.CrossEntropyLoss(weight=weights)
            loss = loss_fn(logits, labels)
        return (loss, outputs) if return_outputs else loss


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def make_text(item, task_name):
    text = item.get("data", "")
    extracted = item.get("gemini_extracted_text", "")
    if task_name != "promise_status" and extracted and extracted.strip() != text.strip():
        return f"Report text:\n{text}\n\nPDF extracted text:\n{extracted}"
    return text


def make_dataset(items, task_name, label_map):
    texts = []
    labels = []
    for item in items:
        texts.append(make_text(item, task_name))
        labels.append(label_map[item.get(task_name, "")])
    return Dataset.from_dict({"text": texts, "label": labels})


def build_class_weights(labels, n_classes, manual_weights):
    if manual_weights:
        return [manual_weights[index] for index in range(n_classes)]

    counts = Counter(labels)
    total = sum(counts.values())
    return [total / (n_classes * counts[index]) for index in range(n_classes)]


def _normalize_weight_label(label):
    return str(label).strip().lower().replace(" ", "")


def parse_manual_weights(raw, id_to_label):
    if raw is None:
        return None
    raw = str(raw).strip()
    if not raw:
        return None
    if raw.lower() in {"auto", "balanced", "none"}:
        return None

    n_classes = len(id_to_label)
    pieces = [piece.strip() for piece in raw.split(",") if piece.strip()]
    if not pieces:
        return None

    if all(":" not in piece for piece in pieces):
        if len(pieces) != n_classes:
            raise ValueError(
                f"Expected {n_classes} positional class weights, got {len(pieces)}: {raw}"
            )
        weights = {}
        for index, value_text in enumerate(pieces):
            try:
                value = float(value_text)
            except ValueError as exc:
                raise ValueError(f"Invalid class weight at index {index}: {value_text}") from exc
            if value <= 0:
                raise ValueError(f"Class weight must be positive at index {index}: {value}")
            weights[index] = value
        return weights

    if not all(":" in piece for piece in pieces):
        raise ValueError(f"Manual weights must be either positional or label-keyed: {raw}")

    label_to_index = {}
    for index, label in id_to_label.items():
        normalized = _normalize_weight_label(label)
        if normalized:
            label_to_index[normalized] = index
        if label == "":
            for alias in ("", "n/a", "na", "none", "blank", "empty"):
                label_to_index[_normalize_weight_label(alias)] = index

    weights = {}
    for piece in pieces:
        label_text, value_text = piece.split(":", 1)
        normalized_label = _normalize_weight_label(label_text)
        if normalized_label not in label_to_index:
            allowed = ", ".join(str(id_to_label[index] or "N/A") for index in range(n_classes))
            raise ValueError(f"Unknown class label {label_text!r}; allowed labels: {allowed}")
        index = label_to_index[normalized_label]
        if index in weights:
            raise ValueError(f"Duplicate class weight for label {label_text!r}")
        try:
            value = float(value_text)
        except ValueError as exc:
            raise ValueError(f"Invalid class weight for label {label_text!r}: {value_text}") from exc
        if value <= 0:
            raise ValueError(f"Class weight must be positive for label {label_text!r}: {value}")
        weights[index] = value

    missing = [str(id_to_label[index] or "N/A") for index in range(n_classes) if index not in weights]
    if missing:
        raise ValueError(f"Missing class weights for labels: {', '.join(missing)}")
    return weights


def parse_task_selection(raw):
    selected = [piece.strip() for piece in raw.split(",") if piece.strip()]
    if not selected:
        raise ValueError("--tasks must include at least one task")
    unknown = [task for task in selected if task not in TASKS]
    if unknown:
        raise ValueError(f"Unknown task(s) in --tasks: {', '.join(unknown)}")
    return selected


def task_configs_from_args(args):
    configs = copy.deepcopy(TASKS)
    if args.ps_manual_weights is not None:
        configs["promise_status"]["manual_weights"] = parse_manual_weights(
            args.ps_manual_weights,
            configs["promise_status"]["id_to_label"],
        )
    if args.es_manual_weights is not None:
        configs["evidence_status"]["manual_weights"] = parse_manual_weights(
            args.es_manual_weights,
            configs["evidence_status"]["id_to_label"],
        )
    selected_tasks = parse_task_selection(args.tasks)
    return selected_tasks, configs


def focal_cross_entropy(logits, labels, class_weights=None, gamma=2.0, reduction="mean"):
    import torch.nn.functional as F

    log_probs = F.log_softmax(logits, dim=-1)
    log_pt = log_probs.gather(dim=1, index=labels.view(-1, 1)).squeeze(1)
    pt = log_pt.exp()
    ce = F.nll_loss(log_probs, labels, weight=class_weights, reduction="none")
    loss = ((1.0 - pt) ** gamma) * ce
    if reduction == "none":
        return loss
    if reduction == "sum":
        return loss.sum()
    if reduction == "mean":
        return loss.mean()
    raise ValueError(f"Unsupported reduction: {reduction}")


def compute_metrics(eval_pred):
    preds = np.argmax(eval_pred.predictions, axis=1)
    labels = eval_pred.label_ids
    return {"f1_macro": f1_score(labels, preds, average="macro", zero_division=0)}


def train_task(task_name, config, train_items, dev_items, output_root, args):
    label_map = config["labels"]
    id_to_label = config["id_to_label"]
    n_classes = len(id_to_label)
    task_root = output_root / task_name
    checkpoint_dir = task_root / "checkpoints"
    model_dir = task_root / "model"

    if (checkpoint_dir.exists() or model_dir.exists()) and not args.resume:
        raise RuntimeError(
            f"{task_name} output already exists at {task_root}; use --resume or a fresh run folder"
        )

    tokenizer = AutoTokenizer.from_pretrained(args.model_id)
    train_ds = make_dataset(train_items, task_name, label_map)
    dev_ds = make_dataset(dev_items, task_name, label_map)

    def tokenize(examples):
        return tokenizer(examples["text"], truncation=True, max_length=args.max_length)

    tok_train = train_ds.map(tokenize, batched=True)
    tok_dev = dev_ds.map(tokenize, batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(
        args.model_id,
        num_labels=n_classes,
    )
    class_weights = build_class_weights(
        train_ds["label"],
        n_classes,
        config["manual_weights"],
    )

    training_args = TrainingArguments(
        output_dir=str(checkpoint_dir),
        learning_rate=args.learning_rate,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        num_train_epochs=args.epochs or config["epochs"],
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,
        fp16=torch.cuda.is_available(),
        warmup_ratio=0.1,
        weight_decay=0.01,
        logging_steps=50,
        report_to="none",
        dataloader_num_workers=0,
        seed=args.seed,
        data_seed=args.seed,
    )

    trainer = WeightedTrainer(
        class_weights=class_weights,
        focal_gamma=args.focal_gamma,
        model=model,
        args=training_args,
        train_dataset=tok_train,
        eval_dataset=tok_dev,
        processing_class=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
        compute_metrics=compute_metrics,
    )
    trainer.train(resume_from_checkpoint=args.resume)
    trainer.save_model(str(model_dir))
    tokenizer.save_pretrained(str(model_dir))

    preds_output = trainer.predict(tok_dev)
    preds = np.argmax(preds_output.predictions, axis=1)
    labels = preds_output.label_ids
    f1 = f1_score(labels, preds, average="macro", zero_division=0)
    report = classification_report(
        labels,
        preds,
        labels=list(range(n_classes)),
        target_names=[id_to_label[index] for index in range(n_classes)],
        digits=4,
        zero_division=0,
    )
    (task_root / "internal_dev_report.txt").write_text(report, encoding="utf-8")
    return {
        "task": task_name,
        "model_dir": str(model_dir),
        "checkpoint_dir": str(checkpoint_dir),
        "internal_dev_macro_f1": f1,
        "internal_train_rows": len(train_items),
        "internal_dev_rows": len(dev_items),
        "class_weights": class_weights,
        "loss": "class_weighted_focal" if args.focal_gamma > 0 else "class_weighted_cross_entropy",
        "focal_gamma": args.focal_gamma,
    }


def parse_args():
    parser = argparse.ArgumentParser(
        description="Train fold-local PS/ES BERT models using only the fold train split."
    )
    parser.add_argument("--train", required=True, help="Fold train_grouped_enhanced.json")
    parser.add_argument("--output-root", required=True, help="Fold-local BERT output root")
    parser.add_argument("--model-id", default=MODEL_ID)
    parser.add_argument("--seed", type=int, default=1301)
    parser.add_argument("--dev-fraction", type=float, default=0.1)
    parser.add_argument("--epochs", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--learning-rate", type=float, default=3e-5)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--focal-gamma", type=float, default=0.0)
    parser.add_argument(
        "--tasks",
        default="promise_status,evidence_status",
        help="Comma-separated subset of tasks to train: promise_status,evidence_status",
    )
    parser.add_argument(
        "--ps-manual-weights",
        default=None,
        help="Promise-status class weights, positional like '3,0.6' or keyed like 'No:3,Yes:0.6'. Use auto for inverse-balanced.",
    )
    parser.add_argument(
        "--es-manual-weights",
        default=None,
        help="Evidence-status class weights, positional like '8,0.5,1.8' or keyed like 'No:8,Yes:0.5,N/A:1.8'. Use auto for inverse-balanced.",
    )
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def remove_output_root_for_overwrite(output_root):
    resolved = output_root.resolve()
    cwd = Path.cwd().resolve()
    if cwd not in [resolved, *resolved.parents]:
        raise RuntimeError(f"Refusing to overwrite path outside workspace: {resolved}")
    if len(resolved.parts) <= len(cwd.parts) + 1:
        raise RuntimeError(f"Refusing to overwrite broad workspace path: {resolved}")
    shutil.rmtree(resolved)


def main():
    args = parse_args()
    os.environ["ALLOW_LABEL_FEATURES"] = "0"
    selected_tasks, task_configs = task_configs_from_args(args)
    output_root = Path(args.output_root)
    if output_root.exists() and args.overwrite:
        remove_output_root_for_overwrite(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    train_items = load_json(args.train)
    internal_train, internal_dev = split_train_internal_dev(
        train_items,
        label_fields=("promise_status", "evidence_status"),
        dev_fraction=args.dev_fraction,
        seed=args.seed,
    )
    if not internal_dev:
        raise RuntimeError("internal dev split is empty; cannot select a fold-local checkpoint")

    write_json(output_root / "internal_train.json", internal_train)
    write_json(output_root / "internal_dev.json", internal_dev)

    results = []
    for task_name in selected_tasks:
        config = task_configs[task_name]
        results.append(train_task(task_name, config, internal_train, internal_dev, output_root, args))

    summary = {
        "train_file": str(Path(args.train).resolve()),
        "output_root": str(output_root.resolve()),
        "leakage_guard": "Only this fold's train rows are used; fold validation rows are not used for training, checkpoint selection, or early stopping.",
        "seed": args.seed,
        "dev_fraction": args.dev_fraction,
        "loss": "class_weighted_focal" if args.focal_gamma > 0 else "class_weighted_cross_entropy",
        "focal_gamma": args.focal_gamma,
        "selected_tasks": selected_tasks,
        "results": results,
    }
    write_json(output_root / "bert_training_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
