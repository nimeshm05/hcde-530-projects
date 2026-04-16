import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
INPUT_CSV = BASE / "responses.csv"
OUTPUT_CSV = BASE / "responses_cleaned.csv"


def tally_product_role(role_upper: str) -> tuple[int, int, int]:
    """Return (ux_designers, ux_researchers, product_managers) for one uppercased role string."""
    r = role_upper
    if "RESEARCH" in r and ("UX" in r or "USER" in r):
        return (0, 1, 0)
    if ("PRODUCT" in r and "MANAGER" in r) or r.endswith(" PM") or r == "PM":
        return (0, 0, 1)
    if ("UX" in r or "UI/UX" in r or "UI & UX" in r) and "DESIGN" in r:
        return (1, 0, 0)
    return (0, 0, 0)


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
            name = (row.get("name") or "").strip()
            if not name:
                continue
            row["name"] = name
            row["role"] = (row.get("role") or "").strip().upper()
            rows_out.append(row)

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_out)

    dropped = total - len(rows_out)
    ux_d = ux_r = pms = 0
    for row in rows_out:
        d, r, p = tally_product_role(row["role"])
        ux_d += d
        ux_r += r
        pms += p

    print(f"Read {total} data row(s), kept {len(rows_out)}, dropped {dropped} (empty name).")
    print(f"Wrote {OUTPUT_CSV}")
    print(
        "Role totals (kept rows): "
        f"UX designers={ux_d}, UX researchers={ux_r}, product managers={pms}"
    )


if __name__ == "__main__":
    main()
