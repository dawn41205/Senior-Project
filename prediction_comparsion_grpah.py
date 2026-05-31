import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics import f1_score

# =========================================
# 設定
# =========================================
WEEK="week13_5"
BASE_DIR = f"dataset/week13/{WEEK}"
VAL_FILE = f"{BASE_DIR}/val_grouped.json"
PRED1_FILE = f"{BASE_DIR}/bert/bert_prediction.json"
PRED2_FILE = f"{BASE_DIR}/LLM/LLM_pipeline_pred_{WEEK}.json"

FIELDS = [
    "promise_status",
    "verification_timeline",
    "evidence_status",
    "evidence_quality"
]

WEIGHTS = [0.2, 0.15, 0.3, 0.35]

# =========================================
# Labels
# =========================================

LABELS_MAP = {
    "promise_status": ["Yes", "No"],
    "verification_timeline": [
        "already",
        "within_2_years",
        "between_2_and_5_years",
        "more_than_5_years",
        "N/A"
    ],
    "evidence_status": ["Yes", "No", "N/A"],
    "evidence_quality": ["Clear", "Not Clear", "Misleading", "N/A"]
}

DEFAULT_LABELS = {
    "promise_status": "N/A",
    "verification_timeline": "N/A",
    "evidence_status": "N/A",
    "evidence_quality": "N/A"
}

# =========================================
# 讀檔
# =========================================

def load_json_dict(path):
    path = Path(path)
    if not path.exists():
        print(f"❌ 檔案不存在: {path}")
        return None

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {
        str(item["id"]): item
        for item in data
    }

# =========================================
# validate
# =========================================

def validate_prediction_labels(pred_dict, name="Prediction"):
    print("\n==============================================")
    print(f"Validating {name} labels...")
    print("==============================================")

    error_count = 0
    for doc_id, obj in pred_dict.items():
        for field in FIELDS:
            value = obj.get(field, DEFAULT_LABELS[field])
            if value not in LABELS_MAP[field]:
                print(f"[ERROR] id={doc_id} {field}='{value}' invalid")
                error_count += 1

    if error_count == 0:
        print(f"✅ All {name} labels are valid")
    else:
        print(f"❌ Found {error_count} invalid labels in {name}")

# =========================================
# F1
# =========================================

def get_weighted_f1(pred_dict, true_dict, name="Model"):
    print(f"\nCalculating F1 for {name}...")
    field_scores = []
    macro_f1s = []

    for field, weight in zip(FIELDS, WEIGHTS):
        y_true, y_pred = [], []
        labels = LABELS_MAP[field]

        for doc_id, true_item in true_dict.items():
            pred_item = pred_dict.get(doc_id, {})
            
            # 1. 取得真實標籤，若不存在則給予預設值
            true_val = true_item.get(field, DEFAULT_LABELS[field])
            # 【核心修改】：如果真值是空字串 ""，自動對應轉換為 "N/A"
            if true_val == "":
                true_val = "N/A"
                
            # 2. 取得預測標籤，若不存在則給予預設值
            pred_val = pred_item.get(field, DEFAULT_LABELS[field])
            # （保險起見，如果預測結果也有出現 ""，也一併轉為 "N/A"）
            if pred_val == "":
                pred_val = "N/A"

            y_true.append(true_val)
            y_pred.append(pred_val)

        score = f1_score(
            y_true, y_pred,
            labels=labels,
            average="macro",
            zero_division=0
        )

        macro_f1s.append(score)
        field_scores.append(score * weight)
        print(f" - [{field}] F1={score:.4f} (w={weight})")

    total_f1 = sum(field_scores)
    return total_f1, macro_f1s

# =========================================
# main
# =========================================

def main():
    print("==============================================")
    print("Loading data...")
    print("==============================================")

    val_data = load_json_dict(VAL_FILE)
    pred1_dict = load_json_dict(PRED1_FILE)
    pred2_dict = load_json_dict(PRED2_FILE)

    # 必要的檔案檢查
    if val_data is None:
        print("❌ 缺少 validation file")
        return
    if pred1_dict is None and pred2_dict is None:
        print("❌ 兩個預測檔案都不存在，無法進行評估")
        return

    # =========================================
    # 驗證與計算各別模型 F1
    # =========================================
    
    # 處理 Model 1 (BERT)
    if pred1_dict:
        validate_prediction_labels(pred1_dict, "BERT Prediction")
        total_f1_p1, macro_f1s_p1 = get_weighted_f1(pred1_dict, val_data, "BERT")
        print(f"➡️ BERT Weighted F1: {total_f1_p1:.4f}")
    else:
        total_f1_p1, macro_f1s_p1 = 0.0, [0.0] * len(FIELDS)

    # 處理 Model 2
    if pred2_dict:
        validate_prediction_labels(pred2_dict, "LLM Prediction ")
        total_f1_p2, macro_f1s_p2 = get_weighted_f1(pred2_dict, val_data, "LLM")
        print(f"➡️ LLM Weighted F1: {total_f1_p2:.4f}")
    else:
        total_f1_p2, macro_f1s_p2 = 0.0, [0.0] * len(FIELDS)

    # Baseline 資料
    baseline_f1s = [0.728, 0.461, 0.596, 0.443]
    baseline_weighted_avg = sum([s * w for s, w in zip(baseline_f1s, WEIGHTS)])

    # =========================================
    # 繪圖 (三方對比)
    # =========================================
    x = np.arange(len(FIELDS))
    width = 0.25  # 縮小寬度以容納三根柱子

    fig, ax = plt.subplots(figsize=(18, 10), dpi=150)
    # Model 1 Bars
    bars_p1 = ax.bar(
        x - width,
        macro_f1s_p1,
        width,
        label=f'BERT (Weighted Avg: {total_f1_p1:.4f})',
        color='steelblue',
        alpha=0.9
    )

    # Model 2 Bars
    bars_p2 = ax.bar(
        x,
        macro_f1s_p2,
        width,
        label=f'LLM (Weighted Avg: {total_f1_p2:.4f})',
        color='mediumseagreen',
        alpha=0.9
    )

    # Baseline Bars
    bars_baseline = ax.bar(
        x + width,
        baseline_f1s,
        width,
        label=f'Official Baseline (Weighted Avg: {baseline_weighted_avg:.4f})',
        color='darkorange',
        alpha=0.9
    )

    # 標數值函式
    def autolabel(bars):
        for bar in bars:
            height = bar.get_height()
            if height > 0:  # 避免畫出 0 的標籤
                ax.annotate(
                    f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    fontsize=9,
                    fontweight='bold'
                )

    autolabel(bars_p1)
    autolabel(bars_p2)
    autolabel(bars_baseline)

    # 圖表設定
    ax.set_xlabel("Task Categories", fontsize=12)
    ax.set_ylabel("Macro F1 Score", fontsize=12)
    ax.set_title(
         f"Performance Comparison:{WEEK}\n"
         f"BERT: {total_f1_p1:.4f}  |  LLM: {total_f1_p2:.4f}  |  Baseline: {baseline_weighted_avg:.4f}", 
         fontsize=14, 
         fontweight='bold', 
         pad=20
     )
    
    ax.set_xticks(x)
    ax.set_xticklabels(
        [f"{f}\n(w={w})" for f, w in zip(FIELDS, WEIGHTS)],
        fontsize=10
    )
    ax.set_ylim(0, 1.1)

    # 繪製各自的加權平均水平線
    if pred1_dict:
        ax.axhline(total_f1_p1, color='steelblue', linestyle='--', linewidth=1.5, alpha=0.6)
    if pred2_dict:
        ax.axhline(total_f1_p2, color='mediumseagreen', linestyle='--', linewidth=1.5, alpha=0.6)
    ax.axhline(baseline_weighted_avg, color='darkorange', linestyle='--', linewidth=1.5, alpha=0.6)

    ax.legend(loc='upper right', frameon=True, shadow=True, fontsize=10)
    ax.grid(True, axis='y', alpha=0.2)

    plt.tight_layout()

    # 儲存圖片
    plt.savefig(
        f"{BASE_DIR}/f1_scores_comparison.png",
        dpi=400,
        bbox_inches='tight'
    )    
    print("\n📊 圖表已輸出: f1_scores_comparison.png")

if __name__ == "__main__":
    main()