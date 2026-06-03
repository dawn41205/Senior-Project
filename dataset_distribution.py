import json
from collections import Counter

import matplotlib.pyplot as plt

# =========================
# 設定
# =========================
PATH="dataset"
TRAIN_FILE = f"{PATH}/vpesg4k_train_1000.json"
VAL_FILE = f"{PATH}/vpesg4k_val_1000.json"

EVAL_FIELDS = {
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


# =========================
# 印出分布
# =========================

def print_distribution(data, name):

    print(f"\n{name}")
    print("=" * 50)

    for field, labels in EVAL_FIELDS.items():

        counts = Counter(item[field] for item in data)
        total = len(data)

        print(f"\n{field}")

        for label in labels:

            count = counts.get(label, 0)
            pct = count / total * 100

            print(
                f"{label:<20}"
                f"{count:>5}"
                f" ({pct:6.2f}%)"
            )


# =========================
# 畫 Train vs Val 分布圖
# =========================

def plot_train_val_distribution(
    train_data,
    val_data,
    save_path=f"{PATH}/train_val_distribution.png"
):

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    fig.suptitle(
        "Train vs Validation Label Distribution",
        fontsize=16,
        fontweight="bold"
    )

    for idx, (field, labels) in enumerate(EVAL_FIELDS.items()):

        ax = axes[idx // 2][idx % 2]

        train_counts = Counter(
            item[field]
            for item in train_data
        )

        val_counts = Counter(
            item[field]
            for item in val_data
        )

        train_values = [
            train_counts.get(label, 0)
            for label in labels
        ]

        val_values = [
            val_counts.get(label, 0)
            for label in labels
        ]

        x = range(len(labels))
        width = 0.4

        train_bars = ax.bar(
            [i - width / 2 for i in x],
            train_values,
            width,
            label="Train"
        )

        val_bars = ax.bar(
            [i + width / 2 for i in x],
            val_values,
            width,
            label="Val"
        )

        ax.set_title(
            field,
            fontsize=12,
            fontweight="bold"
        )

        ax.set_xlabel("Label")
        ax.set_ylabel("Number")

        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, rotation=30)

        ax.legend()

        train_total = sum(train_values)
        val_total = sum(val_values)

        # Train 標註
        for bar in train_bars:

            count = int(bar.get_height())

            pct = (
                count / train_total * 100
                if train_total
                else 0
            )

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                count,
                f"{count}\n({pct:.1f}%)",
                ha="center",
                va="bottom",
                fontsize=8
            )

        # Val 標註
        for bar in val_bars:

            count = int(bar.get_height())

            pct = (
                count / val_total * 100
                if val_total
                else 0
            )

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                count,
                f"{count}\n({pct:.1f}%)",
                ha="center",
                va="bottom",
                fontsize=8
            )

    plt.tight_layout()

    plt.savefig(
        save_path,
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()

    print(f"\nSaved -> {save_path}")


# =========================
# Main
# =========================

def main():

    with open(TRAIN_FILE, "r", encoding="utf-8") as f:
        train_data = json.load(f)

    with open(VAL_FILE, "r", encoding="utf-8") as f:
        val_data = json.load(f)

    print(f"Train size: {len(train_data)}")
    print(f"Val size: {len(val_data)}")

    print_distribution(
        train_data,
        "TRAIN"
    )

    print_distribution(
        val_data,
        "VAL"
    )

    plot_train_val_distribution(
        train_data,
        val_data
    )


if __name__ == "__main__":
    main()