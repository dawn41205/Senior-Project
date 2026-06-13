import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.metrics import f1_score

# =========================================
# 設定
# =========================================


BASE_DIR = f"dataset/test_prediction/"
VAL_FILE = f"dataset/vpesg4k_val_1000.json"
pBERT= f"6-11/bert/4-0.5812947"
pLLM=f"6-12/LLM/1-0.5487401"
PRED1_FILE = f"{BASE_DIR}/{pBERT}/test_prediction_with_confidence.csv"
PRED2_FILE = f"{BASE_DIR}/{pLLM}/test_prediction_with_confidence.csv"
PRED3_FILE = f"{BASE_DIR}/merge/{pBERT} merge {pLLM}/prediction_merged.csv"


FIELDS = [
    "promise_status",
    "verification_timeline",
    "evidence_status",
    "evidence_quality"
]

WEIGHTS = [0.2, 0.15, 0.3, 0.35]
CONF_MARGIN = 0.05
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
    "promise_status": "No",
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
def load_csv_dict(path):

    path = Path(path)

    if not path.exists():
        print(f"❌ 檔案不存在: {path}")
        return None

    df = pd.read_csv(path)

    return {
        str(row["id"]): row.to_dict()
        for _, row in df.iterrows()
    }
# =========================================
# merge
# =========================================

def merge_predictions(pred1_dict, pred2_dict):

    merged = {}

    update_count = 0

    for doc_id, obj1 in pred1_dict.items():

        obj2 = pred2_dict.get(doc_id, {})

        merged_obj = {
            "id": obj1["id"]
        }

        # ==============================
        # helper
        # ==============================

        def choose_field(field):

            nonlocal update_count

            value1 = obj1.get(field)
            value2 = obj2.get(field)

            if value2 is None:
                return value1

            if value1 == value2:
                return value1

            conf1 = float(
                obj1.get(
                    f"{field}_confidence",
                    0.0
                )
            )

            conf2 = float(
                obj2.get(
                    f"{field}_confidence",
                    0.0
                )
            )

            if conf2 - conf1 > CONF_MARGIN:
                update_count += 1
                return value2

            return value1

        # ==============================
        # 1. promise_status
        # ==============================

        promise = choose_field(
            "promise_status"
        )

        merged_obj["promise_status"] = promise

        # ==============================
        # Rule 1
        # promise_status = No
        # ==============================

        if promise == "No":

            merged_obj["verification_timeline"] = "N/A"
            merged_obj["evidence_status"] = "N/A"
            merged_obj["evidence_quality"] = "N/A"

            merged[doc_id] = merged_obj
            continue

        # ==============================
        # 2. verification_timeline
        # ==============================

        merged_obj["verification_timeline"] = (
            choose_field(
                "verification_timeline"
            )
        )

        # ==============================
        # 3. evidence_status
        # ==============================

        evidence = choose_field(
            "evidence_status"
        )

        merged_obj["evidence_status"] = evidence

        # ==============================
        # Rule 2
        # evidence_status != Yes
        # ==============================

        if evidence != "Yes":

            merged_obj["evidence_quality"] = "N/A"

            merged[doc_id] = merged_obj
            continue

        # ==============================
        # 4. evidence_quality
        # ==============================

        merged_obj["evidence_quality"] = (
            choose_field(
                "evidence_quality"
            )
        )

        merged[doc_id] = merged_obj

    print("\n==============================================")
    print("Merge Statistics")
    print("==============================================")
    print(f"Updated fields : {update_count}")
    print("==============================================")

    return merged

# =========================================
# validate
# =========================================

def validate_prediction_labels(pred_dict):

    print("\n==============================================")
    print("Validating prediction labels...")
    print("==============================================")

    error_count = 0

    for doc_id, obj in pred_dict.items():

        for field in FIELDS:

            value = obj.get(field, DEFAULT_LABELS[field])

            if value not in LABELS_MAP[field]:

                print(f"[ERROR] id={doc_id} {field}='{value}' invalid")
                error_count += 1

    if error_count == 0:
        print("✅ All prediction labels are valid")
    else:
        print(f"❌ Found {error_count} invalid labels")

# =========================================
# F1
# =========================================

def get_weighted_f1(pred_dict, true_dict, name="Model"):
    
    print(f"\n==============================================")
    print(f"📊 Calculating Macro F1 for {name}...")
    print("==============================================")
    
    field_scores = []
    macro_f1s = []

    for field, weight in zip(FIELDS, WEIGHTS):
        y_true = []
        y_pred = []
        
        labels = LABELS_MAP[field] 

        for doc_id, true_item in true_dict.items():
            pred_item = pred_dict.get(doc_id, {})
            
            # --- 1. 取得真實標籤 (Ground Truth) ---
            true_val = true_item.get(field, DEFAULT_LABELS[field])
            # 處理 pandas 讀取 CSV 可能產生的 NaN、空字串或 None
            if pd.isna(true_val) or str(true_val).strip() in ["", "NaN", "nan", "None"]:
                true_val = DEFAULT_LABELS[field]  # 依據你的設定轉換為 "N/A" 或 "No"
            else:
                true_val = str(true_val).strip()
                
            # --- 2. 取得預測標籤 (Prediction) ---
            pred_val = pred_item.get(field, DEFAULT_LABELS[field])
            if pd.isna(pred_val) or str(pred_val).strip() in ["", "NaN", "nan", "None"]:
                pred_val = DEFAULT_LABELS[field]
            else:
                pred_val = str(pred_val).strip()

            y_true.append(true_val)
            y_pred.append(pred_val)

        # --- 3. 嚴格執行官方的 Macro F1 計算 ---
        # 傳入 labels=labels 確保分母固定（例如 evidence_quality 固定除以 4）
        score = f1_score(
            y_true, 
            y_pred, 
            labels=labels, 
            average="macro", 
            zero_division=0
        )

        macro_f1s.append(score)
        field_scores.append(score * weight)
        print(f" - [{field}] Macro F1 = {score:.4f} (權重 = {weight})")

    # 計算加權總分
    total_f1 = sum(field_scores)
    print(f"➡️ {name} Final Weighted Score: {total_f1:.4f}")
    
    return total_f1, macro_f1s
def build_submission_df(pred_dict):

    rows = []

    for obj in pred_dict.values():

        rows.append({
            "id": obj["id"],
            "promise_status": obj.get("promise_status", "No"),
            "verification_timeline": obj.get("verification_timeline", "N/A"),
            "evidence_status": obj.get("evidence_status", "N/A"),
            "evidence_quality": obj.get("evidence_quality", "N/A")
        })

    return pd.DataFrame(rows)
# =========================================
# main
# =========================================

def main():

    print("==============================================")
    print("Loading data...")
    print("==============================================")

    val_data = load_json_dict(VAL_FILE)
    pred1_dict = load_csv_dict(PRED1_FILE)
    pred2_dict = load_csv_dict(PRED2_FILE)

    # =========================================
    # 必要檔案檢查
    # =========================================

    if val_data is None:
        print("❌ 缺少 validation file")
        exit(1)

    if pred1_dict is None:
        print("❌ 缺少 prediction1 file")
        exit(1)

    # =========================================
    # merge（pred2 optional）
    # =========================================

    if pred2_dict is not None:
        print("🔀 使用 prediction2 進行 merge")

        predicts_dict = merge_predictions(
            pred1_dict,
            pred2_dict
        )

    else:
        print("ℹ️ 僅使用 prediction1（不 merge）")
        predicts_dict = pred1_dict

    # =========================================
    # validate
    # =========================================

    validate_prediction_labels(predicts_dict)

    # =========================================
    # save CSV (自動創建實體資料夾)
    # =========================================

    output_df = build_submission_df(predicts_dict)
    output_df = output_df.sort_values(by="id")

    out_file = Path(PRED3_FILE)
    
    out_file.parent.mkdir(parents=True, exist_ok=True)

    output_df.to_csv(
        out_file,
        index=False,
        encoding="utf-8-sig"
    )

    # =========================================
    # F1
    # =========================================

    total_f1, macro_f1s = get_weighted_f1(
        predicts_dict,
        val_data
    )
    print(f"\n==============================================")
    print(f"Final Weighted F1: {total_f1:.4f}")
    print(f"==============================================")


    baseline_f1s = [0.728, 0.461, 0.596, 0.443]

    baseline_weighted_avg = sum([
        s * w for s, w in zip(baseline_f1s, WEIGHTS)
    ])

    # =========================================
    # 繪圖
    # =========================================

    x = np.arange(len(FIELDS))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 7))

    # Our model
    bars_current = ax.bar(
        x - width / 2,
        macro_f1s,
        width,
        label='Our Hybrid Pipeline',
        color='steelblue',
        alpha=0.9
    )

    # baseline
    bars_baseline = ax.bar(
        x + width / 2,
        baseline_f1s,
        width,
        label='Official Baseline',
        color='darkorange',
        alpha=0.9
    )

    # =========================================
    # 標數值
    # =========================================

    def autolabel(bars):

        for bar in bars:

            height = bar.get_height()

            ax.annotate(
                f'{height:.3f}',
                xy=(
                    bar.get_x() + bar.get_width() / 2,
                    height
                ),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center',
                va='bottom',
                fontsize=10,
                fontweight='bold'
            )

    autolabel(bars_current)
    autolabel(bars_baseline)

    # =========================================
    # 圖表設定
    # =========================================

    ax.set_xlabel("Task Categories", fontsize=12)
    ax.set_ylabel("Macro F1 Score", fontsize=12)

    ax.set_title(
        f"Performance Comparison\n"
        f"Our Score: {total_f1:.4f} vs Baseline: {baseline_weighted_avg:.4f}",
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

    # =========================================
    # 平均線
    # =========================================

    ax.axhline(
        total_f1,
        color='steelblue',
        linestyle='--',
        linewidth=2,
        alpha=0.7,
        label=f"Our Weighted Avg={total_f1:.4f}"
    )

    ax.axhline(
        baseline_weighted_avg,
        color='darkorange',
        linestyle='--',
        linewidth=2,
        alpha=0.7,
        label=f"Baseline Weighted Avg={baseline_weighted_avg:.4f}"
    )

    ax.legend(loc='upper right', frameon=True, shadow=True)

    ax.grid(True, axis='y', alpha=0.2)

    plt.tight_layout()

    # =========================================
    # save
    # =========================================

    plt.savefig(
        PRED3_FILE,
        dpi=150,
        bbox_inches='tight'
    )

# =========================================
# run
# =========================================

if __name__ == "__main__":
    main()