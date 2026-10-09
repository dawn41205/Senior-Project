import argparse
import json
from pathlib import Path


FORMAL_KEYS = ("id", "data", "pdf_url", "URL", "page_number", "gemini_extracted_text")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def to_formal_item(item):
    out = {}
    for key in FORMAL_KEYS:
        if key in item:
            out[key] = item[key]

    if "pdf_url" not in out and item.get("URL"):
        out["pdf_url"] = item["URL"]
    if "URL" not in out and item.get("pdf_url"):
        out["URL"] = item["pdf_url"]

    return out


def main():
    parser = argparse.ArgumentParser(
        description="Create a formal-test-like input JSON by removing annotation/answer fields."
    )
    parser.add_argument("--input", default="merge/val_grouped_enhanced.json")
    parser.add_argument("--output", default="merge/val_formal_input.json")
    args = parser.parse_args()

    source = load_json(args.input)
    formal = [to_formal_item(item) for item in source]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(output_path, formal)

    with_text = sum(1 for item in formal if item.get("gemini_extracted_text"))
    with_url = sum(1 for item in formal if item.get("pdf_url") or item.get("URL"))
    print(f"Wrote {output_path}")
    print(f"rows={len(formal)} gemini_extracted_text={with_text} url={with_url}")
    print("kept_keys=" + ",".join(FORMAL_KEYS))


if __name__ == "__main__":
    main()
