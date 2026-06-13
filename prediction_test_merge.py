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
pBERT = f"6-11/bert/4-0.5812947"
pLLM = f"6-12/LLM/1-0.5487401"
PRED1_FILE = f"{BASE_DIR}/{pBERT}/test_prediction_with_confidence.csv"
PRED2_FILE = f"{BASE_DIR}/{pLLM}/test_prediction_with_confidence.csv"
PRED3_FILE = f"{BASE_DIR}/merge/BERT 6-11-4 merge LLM 6-12-1/prediction_merged.csv"

FIELDS = [
    "promise_status",
    "verification_timeline",
    "evidence_status",
    "evidence_quality"
]
WEIGHTS = [0.2, 0.15, 0.3, 0.35]
CONF_MARGIN = 0.05

# =========================================
# Labels & Defaults
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
# merge (已修正層級相依邏輯與空值防禦)
# =========================================
def merge_predictions(pred1_dict, pred2_dict):
    merged = {}
    update_count = 0
    
    for doc_id, obj1 in pred1_dict.items():
        obj2 = pred2_dict.get(doc_id, {})
        merged_obj = {
            "id": obj1["id"]
        }
        
        # 內部欄位選擇函數
        def choose_field(field):
            value1 = obj1.get(field, DEFAULT_LABELS[field])
            value2 = obj2.get(field)
            
            # 防禦：處理 Pandas 讀取 CSV 時可能產生的 NaN
            if pd.isna(value1): 
                value1 = DEFAULT_LABELS[field]
            if pd.isna(value2): 
                value2 = None
            
            if value2 is None or value1 == value2:
                return value1, False  # 回傳值與「是否觸發LLM更新」的標記
                
            conf1 = float(obj1.get(f"{field}_confidence", 0.0))
            conf2 = float(obj2.get(f"{field}_confidence", 0.0))
            
            if conf2 - conf1 > CONF_MARGIN:
                return value2, True
            return value1, False

        # -----------------------------------------
        # 1. 決定核心 promise_status
        # -----------------------------------------
        promise, updated = choose_field("promise_status")
        merged_obj["promise_status"] = promise
        if updated:
            update_count += 1
        
        # -----------------------------------------
        # 2. 根據相依規則進行分支填充
        # -----------------------------------------
        if promise == "No":
            # 規則 1：當 promise_status = No，其餘全部強制 N/A
            merged_obj["verification_timeline"] = "N/A"
            merged_obj["evidence_status"] = "N/A"
            merged_obj["evidence_quality"] = "N/A"
        else:
            # 當 promise_status = Yes 時才去評估與更新其他欄位
            timeline, updated = choose_field("verification_timeline")
            merged_obj["verification_timeline"] = timeline
            if updated:
                update_count += 1
            
            evidence, updated = choose_field("evidence_status")
            merged_obj["evidence_status"] = evidence
            if updated:
                update_count += 1
            
            # 規則 2：只有當有證據時，才評估品質；否則強制 N/A
            if evidence == "Yes":
                quality, updated = choose_field("evidence_quality")
                merged_obj["evidence_quality"] = quality
                if updated:
                    update_count += 1
            else:
                merged_obj["evidence_quality"] = "N/A"
                
        merged[doc_id] = merged_obj
        
    print("\n==============================================")
    print("Merge Statistics")
    print("==============================================")
    print(f"Updated fields (Final) : {update_count}")
    print("==============================================")
    return merged

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
    
    # 必要檔案檢查
    if val_data is None:
        print("❌ 缺少 validation file")
        exit(1)
    if pred1_dict is None:
        print("❌ 缺少 prediction1 file")
        exit(1)
        
    # merge（pred2 optional）
    if pred2_dict is not None:
        print("🔀 使用 prediction2 進行 merge")
        predicts_dict = merge_predictions(pred1_dict, pred2_dict)
    else:
        print("ℹ️ 僅使用 prediction1（不 merge）")
        predicts_dict = pred1_dict
   
    # save CSV (自動創建實體資料夾)
    output_df = build_submission_df(predicts_dict)
    output_df = output_df.sort_values(by="id")
    out_file = Path(PRED3_FILE)
    
    out_file.parent.mkdir(parents=True, exist_ok=True)
    output_df.to_csv(
        out_file,
        index=False,
        encoding="utf-8-sig"
    )
    print(f"💾 成果已成功儲存至: {out_file}")
    
# =========================================
# run
# =========================================
if __name__ == "__main__":
    main()