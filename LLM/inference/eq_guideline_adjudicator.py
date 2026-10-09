import re

from dataclasses import dataclass, field

ALIASES = {
    "verification_timeline": {"longer_than_5_years": "more_than_5_years", "N/A": "", None: ""},
    "evidence_status": {"N/A": "", None: ""},
    "evidence_quality": {"N/A": "", None: ""},
}

EXPLICIT_INCOMPLETE_TERMS = [
    "not enough",
    "insufficient",
    "incomplete",
    "unclear",
    "vague",
    "superficial",
    "lacks",
    "lacking",
    "missing",
    "does not show",
    "does not provide",
    "does not demonstrate",
    "does not verify",
    "without showing",
    "without providing",
    "cannot confirm",
    "cannot determine",
    "cannot verify",
    "not directly verify",
    "not directly support",
    "不夠清晰",
    "不清楚",
    "不明確",
    "不足",
    "缺乏",
    "缺少",
    "未說明",
    "未提供",
    "未揭露",
    "未量化",
    "未明確",
    "未顯示",
    "未證明",
    "無法確認",
    "無法判斷",
    "無法驗證",
    "無法直接",
    "不能直接",
    "沒有說明",
    "沒有提供",
    "沒有量化",
    "沒有具體",
    "流於表面",
    "表面",
    "模糊",
]

PROCESS_ONLY_TERMS = [
    "policy",
    "framework",
    "procedure",
    "process",
    "mechanism",
    "initiative",
    "vision",
    "ongoing",
    "continue",
    "improve",
    "promote",
    "enhance",
    "strengthen",
    "制度",
    "政策",
    "流程",
    "機制",
    "架構",
    "方針",
    "願景",
    "倡議",
    "推動",
    "持續",
    "強化",
    "提升",
    "優化",
    "改善",
    "努力",
    "致力",
]

DIRECT_STRONG_PATTERNS = [
    r"\b20\d{2}\b",
    r"\d+(\.\d+)?\s?%",
    r"\d+(\.\d+)?\s?(噸|人次|件|家|場|次|元|萬元|億元|公噸|tco2e|kwh|mwh|gwh)\b",
    r"\b(ISO|SBTi|RE100|TCFD|GRI|SASB|AA1000|SGS|BSI|PwC)\b",
    r"(完成|達成|取得|通過|減少|降低|增加|查證|驗證|認證|揭露|稽核|每年|每季|第三方|外部)",
    r"(completed|achieved|obtained|certified|verified|audited|reduced|increased|third[- ]party)",
]

MISLEADING_TERMS = [
    "misleading",
    "off-topic",
    "irrelevant",
    "unrelated",
    "distract",
    "weakly related",
    "not related",
    "偏題",
    "無關",
    "不相關",
    "轉移注意",
    "誤導",
    "關聯薄弱",
    "關聯很弱",
    "沒有明確關聯",
]

MIXED_LOWEST_TERMS = [
    "mixed clarity",
    "lowest clarity",
    "lowest level",
    "multiple pieces",
    "one weak",
    "some evidence",
    "最低",
    "從嚴",
    "多個證據",
    "多項證據",
    "其中一項",
    "其中一個",
    "部分證據",
    "任一",
]

@dataclass
class EvidenceQualityDecision:
    quality: str
    reason: str
    triggers: list[str] = field(default_factory=list)
    evidence_units: list[str] = field(default_factory=list)

def normalize_label(field, value):
    if value is None:
        value = ""
    return ALIASES.get(field, {}).get(value, value)

def extract_final_answer_segment(text):
    if not text:
        return ""
    lower_text = text.lower()
    idx = lower_text.rfind("reasoning:")
    if idx == -1:
        idx = max(
            lower_text.rfind("promise:"),
            lower_text.rfind("evidence:"),
            lower_text.rfind("quality:"),
        )
    if idx == -1:
        return text[-1400:]
    return text[idx:]

def extract_field_text(text, field_name):
    lines = text.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if line.strip().lower().startswith(f"{field_name.lower()}:"):
            start = idx
    if start is None:
        return ""

    collected = []
    first = lines[start].split(":", 1)[1] if ":" in lines[start] else ""
    collected.append(first.strip())
    for line in lines[start + 1 :]:
        stripped = line.strip()
        if re.match(r"^(reasoning|promise|evidence|timeline|quality)\s*:", stripped, flags=re.I):
            break
        collected.append(stripped)
    return "\n".join(part for part in collected if part)

def split_evidence_units(text):
    evidence = extract_field_text(text, "Evidence") or text
    cleaned = re.sub(r"^\s*(Evidence|證據)\s*:\s*", "", evidence, flags=re.I | re.M)
    pieces = re.split(r"(?:\n+|[；;。]|(?:^|\n)\s*[-*•]\s*)", cleaned)
    units = []
    for piece in pieces:
        unit = " ".join(piece.strip(" -\t\r\n").split())
        if len(unit) >= 4:
            units.append(unit)
    return units

def contains_any(text, terms):
    lower = text.lower()
    return [term for term in terms if term.lower() in lower]

def has_direct_strong_evidence(text):
    return any(re.search(pattern, text, flags=re.I) for pattern in DIRECT_STRONG_PATTERNS)

def has_not_clear_to_clear_support(text):
    metric_or_standard = re.search(
        r"(\d+(\.\d+)?\s?%|\b(ISO|SBTi|RE100|TCFD|GRI|SASB|AA1000|SGS|BSI|PwC)\b)",
        text,
        flags=re.I,
    )
    concrete_action = re.search(
        r"(completed|achieved|obtained|certified|verified|audited|reduced|increased|reached|attained|third[- ]party)",
        text,
        flags=re.I,
    )
    dated = re.search(r"\b20\d{2}\b", text)
    return bool(dated and metric_or_standard and concrete_action)

def adjudicate_evidence_quality(pred, input_item, raw_response):
    current = normalize_label("evidence_quality", pred.get("evidence_quality", ""))
    if pred.get("promise_status") == "No" or normalize_label("evidence_status", pred.get("evidence_status")) == "No":
        return EvidenceQualityDecision("", "pipeline_gating")

    final_segment = extract_final_answer_segment(raw_response)
    evidence_units = split_evidence_units(final_segment)
    inspection_text = "\n".join([final_segment, *evidence_units])

    if current == "Not Clear":
        misleading_hits = contains_any(inspection_text, MISLEADING_TERMS)
        incomplete_hits = contains_any(inspection_text, EXPLICIT_INCOMPLETE_TERMS)
        process_hits = contains_any(inspection_text, PROCESS_ONLY_TERMS)
        if (
            has_not_clear_to_clear_support(inspection_text)
            and not misleading_hits
            and not incomplete_hits
            and not (process_hits and not has_direct_strong_evidence(inspection_text))
        ):
            return EvidenceQualityDecision(
                "Clear",
                "not_clear_direct_concrete_support",
                evidence_units=evidence_units,
            )
        return EvidenceQualityDecision(current, "not_clear_candidate")

    if current != "Clear":
        return EvidenceQualityDecision(current, "not_clear_candidate")

    misleading_hits = contains_any(inspection_text, MISLEADING_TERMS)
    if misleading_hits and not has_direct_strong_evidence(inspection_text):
        return EvidenceQualityDecision("Misleading", "explicit_misleading", misleading_hits, evidence_units)

    incomplete_hits = contains_any(inspection_text, EXPLICIT_INCOMPLETE_TERMS)
    mixed_hits = contains_any(inspection_text, MIXED_LOWEST_TERMS)
    if incomplete_hits:
        reason = "mixed_lowest_clarity" if mixed_hits else "explicit_incomplete"
        return EvidenceQualityDecision("Not Clear", reason, incomplete_hits + mixed_hits, evidence_units)

    process_hits = contains_any(inspection_text, PROCESS_ONLY_TERMS)
    if process_hits and not has_direct_strong_evidence(inspection_text):
        return EvidenceQualityDecision("Not Clear", "process_only_without_concrete", process_hits, evidence_units)

    return EvidenceQualityDecision("Clear", "kept_clear", evidence_units=evidence_units)
