import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.metrics import f1_score

# =========================================
# 設定
# =========================================

WEEK = "week15"
BASE_DIR = f"dataset/{WEEK}/"
VAL_FILE = f"dataset/vpesg4k_val_1000.json"
pBERT = "bert/1"
pLLM = "LLM/1"
PRED1_FILE = f"{BASE_DIR}/{pBERT}/bert_prediction.csv"
PRED2_FILE = f"{BASE_DIR}/{pLLM}/week15_val1000_confidence.csv"

# -----------------------------------------------------------------
# 動態安全路徑處理：將變數中的 "/" 取代為 "_"，避免系統誤判為子目錄
# 這樣一來，資料夾名稱會動態變成： dataset/merge/bert_1 merge LLM_1
# -----------------------------------------------------------------
safe_pBERT = pBERT.replace("/", "_")
safe_pLLM = pLLM.replace("/", "_")
outpath = f"dataset/merge/{safe_pBERT} merge {safe_pLLM}"

# 完整的輸出檔案路徑整合
PRED3_FILE = f"{outpath}/prediction_merged.csv"
PLOT_OUT_FILE = f"{outpath}/f1_scores_comparison.png"

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

    # =========================
    # 清理函數
    # =========================
    def clean_label(value, field):
        if pd.isna(value):
            return DEFAULT_LABELS[field]

        value = str(value).strip()

        if value == "" or value.lower() == "nan":
            return DEFAULT_LABELS[field]

        return value

    # =========================
    # 核心選擇邏輯
    # =========================
    def choose_field(obj1, obj2, field):
        nonlocal update_count

        value1 = clean_label(obj1.get(field), field)
        value2 = clean_label(obj2.get(field), field)

        # ❗ 避免 N/A 覆蓋有效值
        if value1 != "N/A" and value2 == "N/A":
            return value1

        if value2 != "N/A" and value1 == "N/A":
            return value2

        if value1 == value2:
            return value1

        conf1 = float(obj1.get(f"{field}_confidence", 0.0))
        conf2 = float(obj2.get(f"{field}_confidence", 0.0))

        if conf2 - conf1 > CONF_MARGIN:
            update_count += 1
            return value2

        return value1

    # =========================
    # main loop
    # =========================
    for doc_id, obj1 in pred1_dict.items():

        obj2 = pred2_dict.get(doc_id, {})
        merged_obj = {"id": obj1["id"]}

        # 1. promise_status
        promise = choose_field(obj1, obj2, "promise_status")
        merged_obj["promise_status"] = promise

        # =========================
        # Rule 1: No → 全部 N/A
        # =========================
        if promise == "No":
            merged_obj["verification_timeline"] = "N/A"
            merged_obj["evidence_status"] = "N/A"
            merged_obj["evidence_quality"] = "N/A"
            merged[doc_id] = merged_obj
            continue

        # 2. verification_timeline
        merged_obj["verification_timeline"] = choose_field(
            obj1, obj2, "verification_timeline"
        )

        # 3. evidence_status
        evidence = choose_field(obj1, obj2, "evidence_status")
        merged_obj["evidence_status"] = evidence

        # =========================
        # Rule 2: evidence != Yes → quality = N/A
        # =========================
        if evidence != "Yes":
            merged_obj["evidence_quality"] = "N/A"
            merged[doc_id] = merged_obj
            continue

        # 4. evidence_quality
        merged_obj["evidence_quality"] = choose_field(
            obj1, obj2, "evidence_quality"
        )

        merged[doc_id] = merged_obj

    # =========================
    # Debug statistics
    # =========================
    print("\n==============================================")
    print("Merge Statistics")
    print("==============================================")
    print(f"Updated fields : {update_count}")
    print("==============================================")

    # =========================
    # Rule validation（強烈建議保留）
    # =========================
    for doc_id, obj in merged.items():

        if obj["promise_status"] == "Yes":

            if obj["verification_timeline"] == "N/A":
                print(f"[RULE ERROR] {doc_id} verification_timeline=N/A")

            if obj["evidence_status"] == "N/A":
                print(f"[RULE ERROR] {doc_id} evidence_status=N/A")

        if obj["evidence_status"] == "Yes":

            if obj["evidence_quality"] == "N/A":
                print(f"[RULE ERROR] {doc_id} evidence_quality=N/A")

    return merged

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
            
            # 真實標籤處理
            true_val = true_item.get(field, DEFAULT_LABELS[field])
            if pd.isna(true_val) or str(true_val).strip() in ["", "NaN", "nan", "None"]:
                true_val = DEFAULT_LABELS[field]
            else:
                true_val = str(true_val).strip()
                
            # 預測標籤處理
            pred_val = pred_item.get(field, DEFAULT_LABELS[field])
            if pd.isna(pred_val) or str(pred_val).strip() in ["", "NaN", "nan", "None"]:
                pred_val = DEFAULT_LABELS[field]
            else:
                pred_val = str(pred_val).strip()

            y_true.append(true_val)
            y_pred.append(pred_val)

        # 嚴格計算 Macro F1
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

    total_f1 = sum(field_scores)
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

    # 必要的檔案檢查
    if val_data is None:
        print("❌ 缺少 validation file")
        return
    if pred1_dict is None:
        print("❌ 缺少 prediction1 (BERT) file")
        return

    # =========================================
    # 動態建立實體資料夾
    # =========================================
    target_dir = Path(outpath)
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 已成功動態建立/確認目標資料夾: {target_dir}")

    # =========================================
    # 進行資料合併 (Merge)
    # =========================================
    if pred2_dict is not None:
        print("🔀 使用 prediction2 (LLM) 進行混合 Merge...")
        predicts_merged_dict = merge_predictions(pred1_dict, pred2_dict)
    else:
        print("ℹ️ 僅使用 prediction1 (不 merge)")
        predicts_merged_dict = pred1_dict

    # 格式防呆檢查
    validate_prediction_labels(predicts_merged_dict, "Merged Pipeline")

    # 儲存合併結果為 CSV 到動態設定的 outpath 內
    output_df = build_submission_df(predicts_merged_dict)
    output_df = output_df.sort_values(by="id")
    output_df.to_csv(PRED3_FILE, index=False, encoding="utf-8-sig")
    print(f"💾 已成功儲存合併後的 CSV 至: {PRED3_FILE}")

    # 重新讀取剛才生成於 outpath 內的 Merged 檔案
    pred3_dict = load_csv_dict(PRED3_FILE)

    # =========================================
    # 驗證與計算各別模型 F1-Score
    # =========================================
    
    # 1. BERT
    if pred1_dict:
        total_f1_p1, macro_f1s_p1 = get_weighted_f1(pred1_dict, val_data, "BERT")
        print(f"➡️ BERT Final Weighted Score: {total_f1_p1:.4f}")
    else:
        total_f1_p1, macro_f1s_p1 = 0.0, [0.0] * len(FIELDS)

    # 2. LLM
    if pred2_dict:
        total_f1_p2, macro_f1s_p2 = get_weighted_f1(pred2_dict, val_data, "LLM")
        print(f"➡️ LLM Final Weighted Score: {total_f1_p2:.4f}")
    else:
        total_f1_p2, macro_f1s_p2 = 0.0, [0.0] * len(FIELDS)

    # 3. Merged Pipeline
    if pred3_dict:
        total_f1_p3, macro_f1s_p3 = get_weighted_f1(pred3_dict, val_data, "Merged")
        print(f"➡️ Merged Final Weighted Score: {total_f1_p3:.4f}")
    else:
        total_f1_p3, macro_f1s_p3 = 0.0, [0.0] * len(FIELDS)

    # 4. Baseline
    baseline_f1s = [0.728, 0.461, 0.596, 0.443]
    baseline_weighted_avg = sum([s * w for s, w in zip(baseline_f1s, WEIGHTS)])

    # =========================================
    # 繪圖對比 (四合一長條圖)
    # =========================================
    x = np.arange(len(FIELDS))
    width = 0.2
    fig, ax = plt.subplots(figsize=(20, 10), dpi=150)

    # 各模型長條分布
    bars_p1 = ax.bar(x - 1.5 * width, macro_f1s_p1, width, label=f'BERT ({total_f1_p1:.4f})', color='steelblue')
    bars_p2 = ax.bar(x - 0.5 * width, macro_f1s_p2, width, label=f'LLM ({total_f1_p2:.4f})', color='mediumseagreen')
    bars_p3 = ax.bar(x + 0.5 * width, macro_f1s_p3, width, label=f'Merged ({total_f1_p3:.4f})', color='crimson')
    bars_baseline = ax.bar(x + 1.5 * width, baseline_f1s, width, label=f'Baseline ({baseline_weighted_avg:.4f})', color='darkorange')

    # 標數值
    def autolabel(bars):
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.annotate(
                    f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9, fontweight='bold'
                )

    autolabel(bars_p1)
    autolabel(bars_p2)
    autolabel(bars_p3)
    autolabel(bars_baseline)

    # 圖表裝飾設定
    ax.set_xlabel("Task Categories", fontsize=12)
    ax.set_ylabel("Macro F1 Score", fontsize=12)
    ax.set_title(
        f"Performance Comparison ({WEEK})\n"
        f"BERT={total_f1_p1:.4f} | "
        f"LLM={total_f1_p2:.4f} | "
        f"Merged={total_f1_p3:.4f} | "
        f"Baseline={baseline_weighted_avg:.4f}",
        fontsize=15, fontweight='bold', pad=20
    )
    
    ax.set_xticks(x)
    ax.set_xticklabels([f"{f}\n(w={w})" for f, w in zip(FIELDS, WEIGHTS)], fontsize=10)
    ax.set_ylim(0, 1.1)

    # 基準水平線
    ax.axhline(total_f1_p1, color='steelblue', linestyle='--', alpha=0.4)
    ax.axhline(total_f1_p2, color='mediumseagreen', linestyle='--', alpha=0.4)
    ax.axhline(total_f1_p3, color='crimson', linestyle='--', alpha=0.5, linewidth=2)
    ax.axhline(baseline_weighted_avg, color='darkorange', linestyle='--', alpha=0.4)

    ax.legend(loc='upper right', frameon=True, shadow=True, fontsize=10)
    ax.grid(True, axis='y', alpha=0.2)
    plt.tight_layout()

    # 儲存圖表到動態指定的 outpath 中
    plt.savefig(PLOT_OUT_FILE, dpi=400, bbox_inches='tight')    
    plt.close()
    print(f"\n📊 比較圖表已輸出至: {PLOT_OUT_FILE}")

if __name__ == "__main__":
    main()