import json
import os
import re
from collections import Counter

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# =========================
# 設定
# =========================
WEEK = "week14"

INPUT_FILE = os.path.join("dataset", "vpesg4k_train_1000.json")
OUTPUT_DIR = os.path.join("dataset", WEEK)

N_SPLITS = 5
TEST_SIZE = 0.2
BASE_RANDOM_STATE = 42

EVAL_FIELDS = {
    "promise_status": ["Yes", "No"],
    "verification_timeline": [
        "already",
        "within_2_years",
        "between_2_and_5_years",
        "more_than_5_years",
        ""
    ],
    "evidence_status": ["Yes", "No", ""],
    "evidence_quality": ["Clear", "Not Clear", "Misleading", ""]
}

# =========================
# 找已有 split 數量
# =========================

def get_next_split_index(output_dir, week):

    if not os.path.exists(output_dir):
        return 1

    pattern = re.compile(rf"{week}_(\d+)")

    existing = []

    for name in os.listdir(output_dir):
        match = pattern.match(name)

        if match:
            existing.append(int(match.group(1)))

    if not existing:
        return 1

    return max(existing) + 1

# =========================
# 畫圖
# =========================

def plot_label_distribution(train_data, save_path):

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Training data label distribution", fontsize=16, fontweight='bold')

    axes = axes.flatten()

    for idx, (field, labels) in enumerate(EVAL_FIELDS.items()):

        ax = axes[idx]

        counts = Counter(d[field] for d in train_data)
        ordered_counts = {label: counts.get(label, 0) for label in labels}

        colors = sns.color_palette("husl", len(labels))

        bars = ax.bar(
            list(ordered_counts.keys()),
            list(ordered_counts.values()),
            color=colors
        )

        ax.set_title(field, fontsize=12, fontweight='bold')
        ax.set_xlabel("Label")
        ax.set_ylabel("Number")
        ax.tick_params(axis='x', rotation=30)

        total = sum(ordered_counts.values())

        for bar, (label, count) in zip(bars, ordered_counts.items()):

            pct = count / total * 100 if total > 0 else 0

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 1,
                f"{count}\n({pct:.1f}%)",
                ha='center',
                va='bottom',
                fontsize=9
            )

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()

# =========================
# 主程式
# =========================

def main():

    print("Loading data...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Total samples: {len(data)}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 取得接續 index
    start_idx = get_next_split_index(OUTPUT_DIR, WEEK)

    print(f"Start split index: {start_idx}")

    for i in range(N_SPLITS):

        split_id = start_idx + i
        random_state = BASE_RANDOM_STATE + i

        print("\n======================================")
        print(f"Split {split_id} | random_state={random_state}")
        print("======================================")

        train_data, val_data = train_test_split(
            data,
            test_size=TEST_SIZE,
            random_state=random_state,
            shuffle=True
        )

        print(f"Train: {len(train_data)} | Val: {len(val_data)}")

        split_dir = os.path.join(OUTPUT_DIR, f"{WEEK}_{split_id}")
        os.makedirs(split_dir, exist_ok=True)

        # save json
        with open(os.path.join(split_dir, "train_grouped.json"), "w", encoding="utf-8") as f:
            json.dump(train_data, f, ensure_ascii=False, indent=4)

        with open(os.path.join(split_dir, "val_grouped.json"), "w", encoding="utf-8") as f:
            json.dump(val_data, f, ensure_ascii=False, indent=4)

        # plot
        plot_path = os.path.join(split_dir, "label_distribution.png")
        plot_label_distribution(train_data, plot_path)

        print(f"Saved -> {split_dir}")

if __name__ == "__main__":
    main()