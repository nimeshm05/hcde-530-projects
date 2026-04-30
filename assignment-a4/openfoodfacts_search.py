"""HCDE 530 A4: call Open Food Facts search API and print/save a few fields per product."""

import csv
import json
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import certifi

    _SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CONTEXT = ssl.create_default_context()

# Open Food Facts v2 search: filter products in the database (not full-text search on v2).
# This base URL asks the public server for a page of matching products as JSON.
SEARCH_URL = "https://world.openfoodfacts.org/api/v2/search"

# Where we write a small CSV next to this script (easy to open in Excel or a notebook).
OUTPUT_CSV = Path(__file__).resolve().parent / "openfoodfacts_search_sample.csv"


def fetch_search_page(params: dict) -> dict:
    """Build the query string, GET the URL, and parse JSON into a Python dict."""
    qs = urllib.parse.urlencode(params)
    url = f"{SEARCH_URL}?{qs}"
    last_err: Exception | None = None
    # The public server sometimes returns 503; retry with a fresh Request each time.
    for attempt in range(1, 6):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60, context=_SSL_CONTEXT) as resp:
                # The API returns UTF-8 JSON with keys like count, page, products, etc.
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (502, 503, 504) and attempt < 5:
                time.sleep(2.0 * attempt)
                continue
            raise
    assert last_err is not None
    raise last_err


def main() -> None:
    # The following code is the main function that fetches the search page and prints the results.
    # The code is a try-except block that catches any errors that occur during the search.
    # Query parameters: English category label plus optional sort (see OFF search tutorial).
    # "fields" limits each product object so the JSON stays small; we still ask for
    # nutrition_grades so each row can show a Nutri-Score letter when OFF has computed it.
    params = {
        "categories_tags_en": "Yogurt",
        "sort_by": "last_modified_t",
        "fields": "code,product_name,nutrition_grades,categories_tags_en",
        "page_size": "10",
        "page": "1",
    }

    try:
        data = fetch_search_page(params)
    except urllib.error.URLError as e:
        raise SystemExit(f"Search request failed: {e}") from e

    # Whole response tells us how many products matched and what slice we got.
    total = data.get("count")
    products = data.get("products") or []

    print("Open Food Facts search (category: Yogurt, sorted by last_modified_t)")
    print(f"Total matches reported by API: {total}")
    print(f"Products on this page: {len(products)}")
    print()

    # We pull at least three fields from each product (Yogurt products):
    # - code: barcode (unique id in OFF)
    # - product_name: what the product is called
    # - nutrition_grades: Nutri-Score letter when OFF has one for that product
    # categories_tags_en is an extra list we summarize as the deepest English category.
    rows: list[tuple[str, str, str, str]] = []
    for p in products:
        code = str(p.get("code", "")).strip()
        name = str(p.get("product_name", "")).strip() or "(no name)"
        grade = str(p.get("nutrition_grades", "")).strip() or "(no grade)"
        tags = p.get("categories_tags_en") or []
        leaf = str(tags[-1]).strip() if tags else "(no category)"

        rows.append((code, name, grade, leaf))
        print(f"{code} | {grade} | {name}")
        print(f"    category (leaf): {leaf}")
        print()

    # The below code writes the rows to a CSV file.
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["code", "product_name", "nutrition_grades", "category_leaf_en"])
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
