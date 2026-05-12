import json
import torch
import warnings
import gc
import numpy as np
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel
from sklearn.metrics import f1_score
from rag_inference import run_rag_inference

BERT_ES_MODEL_DIR = "./bert_es_model"
BERT_ES_LABELS = {0: "No", 1: "Yes", 2: "N/A"}
BERT_PS_MODEL_DIR = "./bert_ps_model"
BERT_PS_LABELS = {0: "No", 1: "Yes"}

warnings.filterwarnings('ignore')

TASKS = ["promise_status", "evidence_status"]
LABEL_MAPS = {
    "promise_status": {0: "No", 1: "Yes"},
    "evidence_status": {0: "No", 1: "Yes", 2: "N/A"}
}

VAL_FILE = "val_grouped.json"

def predict_classification_task(data, task, model_id="BAAI/bge-m3"):
    """ [舊版回退] 負責動態載入底層大模型與套用對應的 Token 輕量級 LoRA Adapter """
    print(f"\n[推論] 載入 {task} 專屬 QLoRA 模型...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    num_labels = len(LABEL_MAPS[task])
    
    # 載入基礎模型 (原生存取)
    base_model = AutoModelForSequenceClassification.from_pretrained(
        model_id,
        num_labels=num_labels,
        device_map="auto"
    )
    
    # 載入經過微調的專屬 Adapter
    adapter_path = f"./adapter_{task}"
    try:
        model = PeftModel.from_pretrained(base_model, adapter_path)
    except Exception as e:
        print(f"無法載入 Adapter: {adapter_path}，請確認是否已經跑過 train_classifier.py! ({e})")
        return {}
        
    model.eval()
    
    predictions_map = {}
    
    for item in tqdm(data, desc=f"Predicting {task}", unit="篇"):
        doc_id = str(item['id'])
        t = item.get('gemini_extracted_text', "")
        if not t: t = item.get("data", "")
            
        inputs = tokenizer(t, return_tensors="pt", truncation=True, max_length=512).to(model.device)
        
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            pred_id = torch.argmax(logits, dim=-1).item()
            
        predictions_map[doc_id] = LABEL_MAPS[task][pred_id]
        
    return predictions_map

def predict_bert_es(data):
    """ 使用 CKIP BERT 全量微調模型推論 evidence_status (取代 QLoRA/BGE-M3) """
    print(f"\n[推論] 載入 CKIP BERT evidence_status 專屬模型...")
    
    tokenizer = AutoTokenizer.from_pretrained(BERT_ES_MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(
        BERT_ES_MODEL_DIR, num_labels=3
    )
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    predictions_map = {}
    
    for item in tqdm(data, desc="BERT ES 推論", unit="篇"):
        doc_id = str(item['id'])
        text = item.get("data", "")
        promise = item.get("promise_string", "")
        
        # ES 需要拼接 promise_string + data（合法：需對比承諾與內文）
        if promise:
            combined = f"承諾：{promise}\n\n報告內容：{text}"
        else:
            combined = text
        
        inputs = tokenizer(combined, return_tensors="pt", truncation=True, max_length=512).to(device)
        
        with torch.no_grad():
            logits = model(**inputs).logits
            pred_id = torch.argmax(logits, dim=-1).item()
        
        predictions_map[doc_id] = BERT_ES_LABELS[pred_id]
    
    return predictions_map

def predict_bert_ps(data):
    """ 使用 CKIP BERT 全量微調模型推論 promise_status """
    print(f"\n[推論] 載入 CKIP BERT promise_status 專屬模型...")
    
    tokenizer = AutoTokenizer.from_pretrained(BERT_PS_MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(
        BERT_PS_MODEL_DIR, num_labels=2
    )
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    predictions_map = {}
    
    for item in tqdm(data, desc="BERT PS 推論", unit="篇"):
        doc_id = str(item['id'])
        text = item.get("data", "")
        # ⚠️ PS 只看 data 內文，禁止看 promise_string（否則 Data Leakage）
        combined = text
        inputs = tokenizer(combined, return_tensors="pt", truncation=True, max_length=512).to(device)
        with torch.no_grad():
            logits = model(**inputs).logits
            pred_id = torch.argmax(logits, dim=-1).item()
        predictions_map[doc_id] = BERT_PS_LABELS[pred_id]
    
    return predictions_map

def get_weighted_f1(predicts_dict, true_dict):
    """ 跟競賽主辦方 baseline.py 相同的評估程式碼 """
    fields = [
        "promise_status", 
        "verification_timeline", 
        "evidence_status", 
        "evidence_quality"
    ]
    # 對應的權重配比 (官方 baseline 設定: promise 0.2, timeline 0.15, evidence_status 0.3, quality 0.35)
    weights = [0.2, 0.15, 0.3, 0.35]
    
    field_scores = []
    
    macro_f1s = []
    
    for f_idx, field in enumerate(fields):
        y_true = []
        y_pred = []
        for doc_id, true_item in true_dict.items():
            # 取對應 ID 的預測，若無則依各題型給預設值
            pred_item = predicts_dict.get(doc_id, {})
            y_true.append(true_item.get(field, ""))
            y_pred.append(pred_item.get(field, ""))
            
        score = f1_score(y_true, y_pred, average="macro", zero_division=0)
        macro_f1s.append(score)
        field_scores.append(score * weights[f_idx])
        print(f" - [{field}] 獨立 F1: {score:.4f} (權重 {weights[f_idx]})")
        
    return sum(field_scores), macro_f1s, fields, weights

def main():
    print("====== ESG Promise Verification: Hybrid Pipeline (BERT + RAG) ======")
    try:
        with open(VAL_FILE, "r", encoding="utf-8") as f:
            val_data = json.load(f)
    except Exception as e:
        print(f"讀取驗證集失敗，請確實執行過 data_splitter.py ({e})")
        return
        
    # 建立真實答案字典，供最後計算分數
    true_dict = {str(item["id"]): item for item in val_data}
    
    # 1. CKIP BERT 分類器推論 (Promise Status)
    import os
    if os.path.exists(BERT_PS_MODEL_DIR):
        print("\n[升級] 使用 CKIP BERT 進行 promise_status 推論")
        pred_promise = predict_bert_ps(val_data)
    else:
        print("\n[回退] CKIP BERT PS 模型不存在，使用舊版 QLoRA")
        pred_promise = predict_classification_task(val_data, "promise_status")
    
    gc.collect()
    torch.cuda.empty_cache()  
    
    # 2. CKIP BERT 分類器推論 (Evidence Status) — 取代 QLoRA/BGE-M3
    if os.path.exists(BERT_ES_MODEL_DIR):
        print("\n[升級] 使用 CKIP BERT 進行 evidence_status 推論")
        pred_evidence = predict_bert_es(val_data)
    else:
        print("\n[回退] CKIP BERT 模型不存在，使用舊版 QLoRA 推論")
        pred_evidence = predict_classification_task(val_data, "evidence_status")
    
    gc.collect()
    torch.cuda.empty_cache()

    # 3. RAG + Gemma-4-31b-it 生成推論 (Timeline & Quality)
    pred_rag = run_rag_inference(val_data)
    
    # 4. 合併所有模組結果
    final_predictions = []
    predicts_dict = {}
    
    print("\n[合併] 對齊所有模型的預測結果...")
    for item in val_data:
        doc_id = str(item['id'])
        
        # 整合 RAG 或給予最保守預設 (N/A)
        rag_res = pred_rag.get(doc_id, {"verification_timeline": "N/A", "evidence_quality": "N/A"})
        
        pred_obj = {
            "id": int(doc_id),
            "promise_status": pred_promise.get(doc_id, "No"),
            "verification_timeline": rag_res["verification_timeline"],
            "evidence_status": pred_evidence.get(doc_id, "N/A"),
            "evidence_quality": rag_res["evidence_quality"]
        }
        
        # ======== 後處理防呆校正規則 (Heuristic Rules) ========
        # 1. 沒承諾 (Promise = No) → 不可能有時程或證據，全部強制 N/A
        if pred_obj["promise_status"] == "No":
            pred_obj["verification_timeline"] = "N/A"
            pred_obj["evidence_status"] = "N/A"
            pred_obj["evidence_quality"] = "N/A"
            
        # 2. 沒有證據 (Evidence = No) → 證據品質無法判斷，強制 N/A
        if pred_obj["evidence_status"] == "No":
            pred_obj["evidence_quality"] = "N/A"
            
        final_predictions.append(pred_obj)
        predicts_dict[doc_id] = pred_obj
        
    # 輸出最終的提交預測檔
    output_file = "prediction.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(final_predictions, f, ensure_ascii=False, indent=4)
        
    print(f"[Done] 預測結果已存至 {output_file}")
    
    # 5. 計算並列出最終競技分數
    print(f"\n[驗證] 計算 Weighted Macro F1 Score...")
    total_f1, macro_f1s, fields, weights = get_weighted_f1(predicts_dict, true_dict)
    
    print(f"\n==============================================")
    print(f"[Result] 綜合加權 F1 分數 (Weighted Macro F1): {total_f1:.4f}")
    print(f"==============================================")

    import matplotlib.pyplot as plt
    import numpy as np
    
    # 官方比賽官方 baseline 分數
    baseline_f1s = [0.784, 0.4870, 0.639, 0.475]
    baseline_weighted_avg = sum([s * w for s, w in zip(baseline_f1s, weights)])
    
    x = np.arange(len(fields))
    width = 0.35  # 柱子寬度

    fig, ax = plt.subplots(figsize=(12, 7))
    
    # 繪製對比柱狀圖 (Baseline 改為橘色)
    bars_current = ax.bar(x - width/2, macro_f1s, width, label='Our Hybrid Pipeline', color='steelblue', alpha=0.9)
    bars_baseline = ax.bar(x + width/2, baseline_f1s, width, label='Official Baseline', color='darkorange', alpha=0.9)

    # 在柱子上加上數字標籤
    def autolabel(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.3f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

    autolabel(bars_current)
    autolabel(bars_baseline)

    ax.set_xlabel("Task Categories", fontsize=12)
    ax.set_ylabel("Macro F1 Score", fontsize=12)
    ax.set_title(f"Performance Comparison: Our Pipeline vs. Official Baseline\nFinal Weighted Score: {total_f1:.4f} (vs. Baseline {baseline_weighted_avg:.4f})", 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{f}\n(w={w})" for f, w in zip(fields, weights)], fontsize=10)
    ax.set_ylim(0, 1.1)
    
    # 加入兩條加權平均水平線
    ax.axhline(total_f1, color='steelblue', linestyle='--', linewidth=2, label=f"Our Weighted Avg={total_f1:.4f}", alpha=0.7)
    ax.axhline(baseline_weighted_avg, color='darkorange', linestyle='--', linewidth=2, label=f"Baseline Weighted Avg={baseline_weighted_avg:.4f}", alpha=0.7)
    
    ax.legend(loc='upper right', frameon=True, shadow=True, fontsize=10)
    ax.grid(True, alpha=0.2, axis='y')

    plt.tight_layout()
    plt.savefig("f1_scores_comparison.png", dpi=150, bbox_inches='tight')
    plt.savefig("f1_scores.png", dpi=150, bbox_inches='tight') 
    print(f"✅ 已更新成績圖表。官方平均分: {baseline_weighted_avg:.4f}")

if __name__ == "__main__":
    main()
