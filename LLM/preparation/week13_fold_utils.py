import random
from collections import defaultdict


FORMAL_KEYS = ("id", "data", "pdf_url", "URL", "page_number", "gemini_extracted_text")


def formal_items(items):
    out = []
    for item in items:
        formal = {key: item[key] for key in FORMAL_KEYS if key in item}
        if "pdf_url" not in formal and item.get("URL"):
            formal["pdf_url"] = item["URL"]
        if "URL" not in formal and item.get("pdf_url"):
            formal["URL"] = item["pdf_url"]
        out.append(formal)
    return out


def split_train_internal_dev(items, label_fields, dev_fraction=0.1, seed=1301):
    if not 0 < dev_fraction < 0.5:
        raise ValueError("dev_fraction must be between 0 and 0.5")

    buckets = defaultdict(list)
    for item in items:
        label_key = tuple(item.get(field, "") for field in label_fields)
        buckets[label_key].append(item)

    rng = random.Random(seed)
    internal_train = []
    internal_dev = []

    for label_key in sorted(buckets, key=lambda value: repr(value)):
        rows = list(buckets[label_key])
        rng.shuffle(rows)
        if len(rows) <= 1:
            dev_count = 0
        else:
            dev_count = max(1, int(round(len(rows) * dev_fraction)))
            dev_count = min(dev_count, len(rows) - 1)
        internal_dev.extend(rows[:dev_count])
        internal_train.extend(rows[dev_count:])

    internal_train.sort(key=lambda item: str(item.get("id", "")))
    internal_dev.sort(key=lambda item: str(item.get("id", "")))
    return internal_train, internal_dev
