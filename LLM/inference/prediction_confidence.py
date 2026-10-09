import csv
import json
import os


LABEL_FIELDS = [
    "id",
    "promise_status",
    "verification_timeline",
    "evidence_status",
    "evidence_quality",
]

CONFIDENCE_VALUE_FIELDS = [
    "promise_status_confidence",
    "verification_timeline_confidence",
    "evidence_status_confidence",
    "evidence_quality_confidence",
]

CONFIDENCE_FIELDS = LABEL_FIELDS + CONFIDENCE_VALUE_FIELDS


def clamp_confidence(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return 0.0
    return max(0.0, min(1.0, value))


def round_confidence(value):
    return round(clamp_confidence(value), 3)


def format_confidence(value):
    text = f"{round_confidence(value):.3f}".rstrip("0").rstrip(".")
    if "." not in text:
        text = f"{text}.0"
    return text


def normalize_confidence_row(item):
    row = {}
    for field in LABEL_FIELDS:
        row[field] = item.get(field, "")
    for field in CONFIDENCE_VALUE_FIELDS:
        row[field] = round_confidence(item.get(field, 0.0))
    return row


def normalize_confidence_rows(predictions):
    return [normalize_confidence_row(item) for item in predictions]


def default_confidence_path(path, suffix):
    root, ext = os.path.splitext(path)
    if not ext:
        ext = suffix
    return f"{root}_with_confidence{ext}"


def write_confidence_json(path, predictions):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(normalize_confidence_rows(predictions), handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def write_confidence_csv(path, predictions):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=CONFIDENCE_FIELDS,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()

        def sort_key(obj):
            try:
                return (0, int(obj["id"]))
            except (TypeError, ValueError):
                return (1, str(obj["id"]))

        for item in sorted(predictions, key=sort_key):
            row = normalize_confidence_row(item)
            for field in CONFIDENCE_FIELDS:
                if field.endswith("_confidence"):
                    row[field] = format_confidence(row.get(field, 0.0))
            writer.writerow({field: row.get(field, "") for field in CONFIDENCE_FIELDS})
