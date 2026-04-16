import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
INPUT_CSV = BASE / "week3_survey_messy.csv"
OUTPUT_CSV = BASE / "week3_survey_cleaned.csv"


def _strip_all(row: dict, fieldnames: list[str]) -> dict:
    out = {}
    for key in fieldnames:
        val = row.get(key)
        out[key] = (val if val is not None else "").strip()
    return out


def _as_int_str_or_empty(s: str) -> str:
    if not s:
        return ""
    try:
        return str(int(s))
    except ValueError:
        return ""


def clean_row(row: dict, fieldnames: list[str]) -> dict | None:
    """Return a cleaned row dict, or None if the row should be dropped."""
    out = _strip_all(row, fieldnames)
    if not out.get("participant_name"):
        return None
    for key in ("role", "department", "primary_tool"):
        if out.get(key):
            out[key] = out[key].title()
    out["experience_years"] = _as_int_str_or_empty(out.get("experience_years", ""))
    out["satisfaction_score"] = _as_int_str_or_empty(out.get("satisfaction_score", ""))
    return out


def main() -> None:
    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise SystemExit(f"No header row found in {INPUT_CSV}")

        rows_out = []
        total = 0
        for row in reader:
            total += 1
            cleaned = clean_row(row, fieldnames)
            if cleaned is not None:
                rows_out.append(cleaned)

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_out)

    dropped = total - len(rows_out)
    print(f"Read {total} data row(s), wrote {len(rows_out)}, dropped {dropped} (empty participant_name).")
    print(f"Wrote {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
