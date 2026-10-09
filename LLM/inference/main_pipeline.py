import csv

import json

import os

import torch

import warnings

import gc

from tqdm import tqdm

from transformers import AutoTokenizer, AutoModelForSequenceClassification

from esg_consistency import apply_consistency_gates

from prediction_confidence import (
    clamp_confidence,
    default_confidence_path,
    write_confidence_csv,
    write_confidence_json,
)

from bert_thresholds import select_label_with_thresholds

from rag_inference import run_rag_inference

BERT_ES_MODEL_DIR = os.environ.get(
    "BERT_ES_MODEL_DIR",
    "./bert_es_model_formal" if os.path.exists("./bert_es_model_formal") else "./bert_es_model_v2",
)

BERT_ES_LABELS = {0: "No", 1: "Yes", 2: ""}

BERT_PS_MODEL_DIR = os.environ.get("BERT_PS_MODEL_DIR", "./bert_ps_model")

BERT_PS_LABELS = {0: "No", 1: "Yes"}

BERT_THRESHOLD_FILE = os.environ.get("BERT_THRESHOLD_FILE", "")

warnings.filterwarnings('ignore')

INPUT_FILE = os.environ.get("INPUT_FILE", os.environ.get("VAL_FILE", "val_grouped.json"))

OUTPUT_FILE = os.environ.get("OUTPUT_FILE", "prediction.json")

OUTPUT_CSV = os.environ.get(
    "OUTPUT_CSV",
    f"{os.path.splitext(OUTPUT_FILE)[0]}.csv",
)

WRITE_CONFIDENCE_OUTPUT = os.environ.get("WRITE_CONFIDENCE_OUTPUT", "1").lower() in {"1", "true", "yes"}

OUTPUT_CONFIDENCE_FILE = os.environ.get(
    "OUTPUT_CONFIDENCE_FILE",
    default_confidence_path(OUTPUT_FILE, ".json"),
)

OUTPUT_CONFIDENCE_CSV = os.environ.get(
    "OUTPUT_CONFIDENCE_CSV",
    default_confidence_path(OUTPUT_CSV, ".csv"),
)

ENABLE_VT_EQ_POSTPROCESS = os.environ.get("ENABLE_VT_EQ_POSTPROCESS", "0").lower() in {"1", "true", "yes"}

OUTPUT_NA_LABEL = os.environ.get("OUTPUT_NA_LABEL", "N/A")

def load_bert_thresholds(path):
    if not path or not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    return {
        task: obj.get("thresholds", {})
        for task, obj in data.get("tasks", {}).items()
    }

BERT_THRESHOLDS = load_bert_thresholds(BERT_THRESHOLD_FILE)

LABEL_ALIASES = {
    "verification_timeline": {
        "longer_than_5_years": "more_than_5_years",
        "N/A": "",
        None: "",
    },
    "evidence_status": {
        "N/A": "",
        None: "",
    },
    "evidence_quality": {
        "N/A": "",
        None: "",
    },
}

def normalize_label(field, value):
    if value is None:
        value = ""
    return LABEL_ALIASES.get(field, {}).get(value, value)

def output_label(field, value):
    value = normalize_label(field, value)
    if field in {"verification_timeline", "evidence_status", "evidence_quality"} and value == "":
        return OUTPUT_NA_LABEL
    return value

STRONG_EVIDENCE_TERMS = [
    "%",
    "％",
    "ISO",
    "GRI",
    "問卷",
    "金額",
    "人數",
    "時數",
    "小時",
    "噸",
    "公噸",
    "仟元",
    "萬元",
    "件",
    "次",
]

def _source_text(item):
    return "\n".join(
        str(item.get(key, ""))
        for key in ("data", "gemini_extracted_text")
    )

def _core_text(item):
    return _source_text(item)

VT_REFERENCE_YEAR = int(os.environ.get("VT_REFERENCE_YEAR", "2024"))

def _has_year_at_or_after(text, min_year):
    import re

    return any(int(year) >= min_year for year in re.findall(r"20\d{2}", text))

def _has_strong_evidence_marker(text):
    import re

    return bool(re.search(r"\d", text)) and any(term in text for term in STRONG_EVIDENCE_TERMS)

PROMISE_TARGET_TERMS = (
    "target",
    "goal",
    "commit",
    "pledge",
    "aim",
    "by ",
    "before",
    "until",
    "net zero",
    "carbon neutral",
    "renewable",
    "reduction",
    "目標",
    "承諾",
    "預計",
    "規劃",
    "達成",
    "以前",
    "之前",
    "年底",
)

ACTION_YEAR_TERMS = (
    "completed",
    "verified",
    "audited",
    "obtained",
    "certified",
    "reported",
    "published",
    "implemented",
    "verification",
    "assurance",
    "查證",
    "驗證",
    "取得",
    "執行",
    "完成",
    "揭露",
    "報告",
)

def _sentences_for_year_scan(text):
    import re

    return [part.strip() for part in re.split(r"[\r\n。.!?；;]+", text or "") if part.strip()]

def extract_promise_target_year(text):
    """Return a target year from promise/goal context, ignoring action-only years."""
    import re

    candidates = []
    for sentence in _sentences_for_year_scan(text):
        years = [int(year) for year in re.findall(r"\b20\d{2}\b", sentence)]
        if not years:
            continue
        lower = sentence.lower()
        has_target_context = any(term.lower() in lower for term in PROMISE_TARGET_TERMS)
        has_action_context = any(term.lower() in lower for term in ACTION_YEAR_TERMS)
        if has_target_context and not (has_action_context and not _has_explicit_target_phrase(lower)):
            candidates.extend(years)
    if not candidates:
        return None
    return max(candidates)

def _has_explicit_target_phrase(text):
    return any(
        phrase in text
        for phrase in (
            "target",
            "goal",
            "commit",
            "pledge",
            "by ",
            "目標",
            "承諾",
            "達成",
            "以前",
            "之前",
        )
    )

def timeline_from_target_year(year, reference_year=VT_REFERENCE_YEAR):
    if year <= reference_year:
        return "already"
    if year <= reference_year + 2:
        return "within_2_years"
    if year <= reference_year + 5:
        return "between_2_and_5_years"
    return "more_than_5_years"

def apply_vt_eq_postprocess(pred_obj, source_item):
    """Optional formal-input-safe VT/EQ fixes.

    Disabled by default. It only reads data generated from formal inputs.
    """
    text = _source_text(source_item)
    target_year = extract_promise_target_year(text)

    if pred_obj.get("verification_timeline") == "already" and target_year:
        target_timeline = timeline_from_target_year(target_year)
        if target_timeline != "already":
            pred_obj["verification_timeline"] = target_timeline

def build_formal_es_text(item):
    text = item.get("data", "")
    extracted = item.get("gemini_extracted_text", "")
    if extracted and extracted.strip() and extracted.strip() != text.strip():
        return f"報告內容：{text}\n\nPDF頁面文字：{extracted}"
    return text

def predict_bert_es(data, return_confidence=False):
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
    confidence_map = {}
    
    for item in tqdm(data, desc="BERT ES 推論", unit="篇"):
        doc_id = str(item['id'])
        text = item.get("data", "")
        combined = build_formal_es_text(item)

        inputs = tokenizer(combined, return_tensors="pt", truncation=True, max_length=512).to(device)
        
        with torch.no_grad():
            logits = model(**inputs).logits
            probs = torch.softmax(logits, dim=-1)
            pred_id = select_label_with_thresholds(
                probs[0].detach().cpu().tolist(),
                BERT_ES_LABELS,
                BERT_THRESHOLDS.get("evidence_status", {}),
            )
        
        predictions_map[doc_id] = BERT_ES_LABELS[pred_id]
        confidence_map[doc_id] = float(probs[0, pred_id].item())
    
    if return_confidence:
        return predictions_map, confidence_map
    return predictions_map

def predict_bert_ps(data, return_confidence=False):
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
    confidence_map = {}
    
    for item in tqdm(data, desc="BERT PS 推論", unit="篇"):
        doc_id = str(item['id'])
        text = item.get("data", "")
        # promise_status 模型只能看到內文，不能看 promise_string，否則會 Data Leakage
        combined = text
        inputs = tokenizer(combined, return_tensors="pt", truncation=True, max_length=512).to(device)
        with torch.no_grad():
            logits = model(**inputs).logits
            probs = torch.softmax(logits, dim=-1)
            pred_id = select_label_with_thresholds(
                probs[0].detach().cpu().tolist(),
                BERT_PS_LABELS,
                BERT_THRESHOLDS.get("promise_status", {}),
            )
        predictions_map[doc_id] = BERT_PS_LABELS[pred_id]
        confidence_map[doc_id] = float(probs[0, pred_id].item())
    
    if return_confidence:
        return predictions_map, confidence_map
    return predictions_map

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def normalize_output_id(doc_id):
    try:
        return int(doc_id)
    except (TypeError, ValueError):
        return doc_id

def write_prediction_json(path, predictions):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(predictions, f, ensure_ascii=False, indent=4)

def write_submission_csv(path, predictions):
    fields = [
        "id",
        "promise_status",
        "verification_timeline",
        "evidence_status",
        "evidence_quality",
    ]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        def sort_key(obj):
            try:
                return (0, int(obj["id"]))
            except (TypeError, ValueError):
                return (1, str(obj["id"]))

        for item in sorted(predictions, key=sort_key):
            writer.writerow({field: output_label(field, item.get(field, "")) for field in fields})

def apply_esg_logic(pred_obj):
    apply_consistency_gates(pred_obj, na_value="")

def main():
    print("====== ESG Promise Verification: Hybrid Pipeline (BERT + RAG/LLM) ======")
    try:
        val_data = load_json(INPUT_FILE)
    except Exception as e:
        print(f"讀取輸入資料失敗，請確認 INPUT_FILE/VAL_FILE 設定正確 ({e})")
        return

    for model_dir in (BERT_PS_MODEL_DIR, BERT_ES_MODEL_DIR):
        if not os.path.isdir(model_dir):
            raise FileNotFoundError(f"Required BERT model directory is missing: {model_dir}")

    pred_promise, pred_promise_conf = predict_bert_ps(val_data, return_confidence=True)
    gc.collect()
    torch.cuda.empty_cache()

    pred_evidence, pred_evidence_conf = predict_bert_es(val_data, return_confidence=True)
    gc.collect()
    torch.cuda.empty_cache()

    pred_rag = run_rag_inference(val_data)

    # 4. 合併所有模組結果
    final_predictions = []
    confidence_predictions = []
    
    print("\n[合併] 對齊所有模型的預測結果...")
    for item in val_data:
        doc_id = str(item['id'])
        
        # 整合 RAG 或給予最保守預設 (N/A)
        rag_res = pred_rag.get(doc_id, {"verification_timeline": "", "evidence_quality": ""})
        
        pred_obj = {
            "id": normalize_output_id(doc_id),
            "promise_status": pred_promise.get(doc_id, "No"),
            "verification_timeline": normalize_label("verification_timeline", rag_res["verification_timeline"]),
            "evidence_status": normalize_label("evidence_status", pred_evidence.get(doc_id, "")),
            "evidence_quality": normalize_label("evidence_quality", rag_res["evidence_quality"])
        }
        confidence_obj = {
            "promise_status": clamp_confidence(pred_promise_conf.get(doc_id, 0.0)),
            "verification_timeline": clamp_confidence(
                rag_res.get("verification_timeline_confidence", 0.55)
            ),
            "evidence_status": clamp_confidence(pred_evidence_conf.get(doc_id, 0.0)),
            "evidence_quality": clamp_confidence(rag_res.get("evidence_quality_confidence", 0.55)),
        }
        if ENABLE_VT_EQ_POSTPROCESS:
            before_post = dict(pred_obj)
            apply_vt_eq_postprocess(pred_obj, item)
            for field in ("verification_timeline", "evidence_quality"):
                if pred_obj.get(field) != before_post.get(field):
                    confidence_obj[field] = min(confidence_obj[field], 0.80)
        before_gate = dict(pred_obj)
        apply_esg_logic(pred_obj)
        for field in ("promise_status", "verification_timeline", "evidence_status", "evidence_quality"):
            if pred_obj.get(field) != before_gate.get(field):
                confidence_obj[field] = min(confidence_obj[field], 0.80)

        output_obj = {
            field: output_label(field, value)
            for field, value in pred_obj.items()
        }
        final_predictions.append(output_obj)
        confidence_predictions.append(
            {
                "id": output_obj["id"],
                "promise_status": output_obj["promise_status"],
                "verification_timeline": output_obj["verification_timeline"],
                "evidence_status": output_obj["evidence_status"],
                "evidence_quality": output_obj["evidence_quality"],
                "promise_status_confidence": clamp_confidence(confidence_obj["promise_status"]),
                "verification_timeline_confidence": clamp_confidence(confidence_obj["verification_timeline"]),
                "evidence_status_confidence": clamp_confidence(confidence_obj["evidence_status"]),
                "evidence_quality_confidence": clamp_confidence(confidence_obj["evidence_quality"]),
            }
        )
        
    # 輸出最終的提交預測檔
    write_prediction_json(OUTPUT_FILE, final_predictions)
    write_submission_csv(OUTPUT_CSV, final_predictions)
    print(f"[Done] 預測結果已存至 {OUTPUT_FILE}")
    print(f"[Done] 正式提交 CSV 已存至 {OUTPUT_CSV}")

    if WRITE_CONFIDENCE_OUTPUT:
        write_confidence_json(OUTPUT_CONFIDENCE_FILE, confidence_predictions)
        write_confidence_csv(OUTPUT_CONFIDENCE_CSV, confidence_predictions)
        print(f"[Done] Confidence JSON: {OUTPUT_CONFIDENCE_FILE}")
        print(f"[Done] Confidence CSV: {OUTPUT_CONFIDENCE_CSV}")


if __name__ == "__main__":
    main()
