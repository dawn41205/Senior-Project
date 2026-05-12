import json
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.metrics import f1_score

# =========================================
# 設定
# =========================================

VAL_FILE = "val_grouped.json"
PRED1_FILE = "prediction.json"
PRED2_FILE = "prediction2.json"

FIELDS_TO_MERGE = [
    "promise_status",
    "verification_timeline"
]

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
        "longer_than_5_years",
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

# =========================================
# merge
# =========================================

def merge_predictions(pred1_dict, pred2_dict, merge_fields):

    merged = {}

    for doc_id, obj in pred1_dict.items():
        merged[doc_id] = dict(obj)

    update_count = 0

    for doc_id, obj in merged.items():

        if doc_id not in pred2_dict:
            continue

        pred2_obj = pred2_dict[doc_id]

        for field in merge_fields:

            if field in pred2_obj:

                if obj.get(field) != pred2_obj[field]:
                    obj[field] = pred2_obj[field]
                    update_count += 1

    print(f"✅ 更新欄位數量: {update_count}")

    return merged

# =========================================
# ESG rule
# =========================================

def apply_esg_logic(pred_dict):

    for obj in pred_dict.values():

        promise = obj.get("promise_status", "No").strip()
        evidence = obj.get("evidence_status", "N/A").strip()

        if promise == "No":
            obj["verification_timeline"] = "N/A"
            obj["evidence_status"] = "N/A"
            obj["evidence_quality"] = "N/A"

        elif evidence == "No":
            obj["evidence_quality"] = "N/A"

    return pred_dict

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

def get_weighted_f1(pred_dict, true_dict):

    field_scores = []
    macro_f1s = []

    for field, weight in zip(FIELDS, WEIGHTS):

        y_true, y_pred = [], []
        labels = LABELS_MAP[field]

        for doc_id, true_item in true_dict.items():

            pred_item = pred_dict.get(doc_id, {})

            y_true.append(true_item.get(field, DEFAULT_LABELS[field]))
            y_pred.append(pred_item.get(field, DEFAULT_LABELS[field]))

        score = f1_score(
            y_true, y_pred,
            labels=labels,
            average="macro",
            zero_division=0
        )

        macro_f1s.append(score)
        field_scores.append(score * weight)

        print(f" - [{field}] F1={score:.4f} (w={weight})")

    return sum(field_scores), macro_f1s, FIELDS, WEIGHTS

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
            pred2_dict,
            FIELDS_TO_MERGE
        )

    else:
        print("ℹ️ 僅使用 prediction1（不 merge）")
        predicts_dict = pred1_dict

    # =========================================
    # ESG logic
    # =========================================

    predicts_dict = apply_esg_logic(predicts_dict)

    # =========================================
    # validate
    # =========================================

    validate_prediction_labels(predicts_dict)

    # =========================================
    # save
    # =========================================

    out_file = "prediction_final_merged.json"

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(
            sorted(predicts_dict.values(), key=lambda x: int(x["id"])),
            f,
            ensure_ascii=False,
            indent=4
        )

    print(f"\n✅ saved: {out_file}")

    # =========================================
    # F1
    # =========================================

    total_f1, macro_f1s, fields, weights = get_weighted_f1(
        predicts_dict,
        val_data
    )

    print(f"\n==============================================")
    print(f"Final Weighted F1: {total_f1:.4f}")
    print(f"==============================================")


    baseline_f1s = [0.728, 0.461, 0.596, 0.443]

    baseline_weighted_avg = sum([
        s * w for s, w in zip(baseline_f1s, weights)
    ])

    # =========================================
    # 繪圖
    # =========================================

    x = np.arange(len(fields))
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
        [f"{f}\n(w={w})" for f, w in zip(fields, weights)],
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

    plt.savefig("f1_scores_comparison.png", dpi=150, bbox_inches='tight')
    plt.savefig("f1_scores.png", dpi=150, bbox_inches='tight')

    print("📊 圖表已輸出: f1_scores_comparison.png / f1_scores.png")
# =========================================
# run
# =========================================

if __name__ == "__main__":
    main()