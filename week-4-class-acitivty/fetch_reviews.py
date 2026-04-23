"""Fetch HCDE 530 week-4 reviews: category and helpful_votes, print and save to CSV."""

import csv
import json
import ssl
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import certifi

    _SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CONTEXT = ssl.create_default_context()

BASE_URL = "https://hcde530-week4-api.onrender.com/reviews/"
PAGE_LIMIT = 100
OUTPUT_CSV = Path(__file__).resolve().parent / "reviews_category_helpful_votes.csv"
TOP50_HELPFUL_CSV = Path(__file__).resolve().parent / "reviews_top50_helpful_votes.csv"


def fetch_page(offset: int, limit: int) -> dict:
    qs = urllib.parse.urlencode({"offset": offset, "limit": limit})
    url = f"{BASE_URL}?{qs}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60, context=_SSL_CONTEXT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_all_reviews() -> list[dict]:
    first = fetch_page(0, PAGE_LIMIT)
    total = int(first["total"])
    reviews = list(first["reviews"])
    offset = int(first.get("offset", 0)) + int(first.get("returned", len(first["reviews"])))

    while offset < total:
        page = fetch_page(offset, PAGE_LIMIT)
        batch = page["reviews"]
        if not batch:
            break
        reviews.extend(batch)
        offset += len(batch)

    return reviews


def _category_helpful_rows(reviews: list[dict]) -> list[tuple[str, int]]:
    rows: list[tuple[str, int]] = []
    for item in reviews:
        category = str(item.get("category", "")).strip()
        votes = item.get("helpful_votes")
        try:
            helpful = int(votes) if votes is not None else 0
        except (TypeError, ValueError):
            helpful = 0
        rows.append((category, helpful))
    return rows


def top_50_highest_helpful_votes(
    reviews: list[dict], output_path: Path | None = None
) -> list[tuple[str, int]]:
    """Return the 50 (category, helpful_votes) rows with the largest helpful_votes; write them to CSV."""
    rows = _category_helpful_rows(reviews)
    rows.sort(key=lambda r: r[1], reverse=True)
    top = rows[:50]
    path = output_path or TOP50_HELPFUL_CSV
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "helpful_votes"])
        writer.writerows(top)
    return top


def main() -> None:
    try:
        reviews = fetch_all_reviews()
    except urllib.error.URLError as e:
        raise SystemExit(f"Failed to fetch reviews: {e}") from e

    rows = _category_helpful_rows(reviews)
    for category, helpful in rows:
        print(f"{category}: {helpful} helpful votes")

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "helpful_votes"])
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} rows to {OUTPUT_CSV}")

    top50 = top_50_highest_helpful_votes(reviews)
    print(f"Wrote {len(top50)} rows (top helpful_votes) to {TOP50_HELPFUL_CSV}")


if __name__ == "__main__":
    main()
