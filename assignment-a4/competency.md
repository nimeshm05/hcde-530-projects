# C4 — APIs and Data Acquisition

I met this competency with `openfoodfacts_search.py` in this folder by building a **yogurt-focused API workflow**. I used the Open Food Facts v2 search endpoint (`GET https://world.openfoodfacts.org/api/v2/search`) and set `categories_tags_en=Yogurt` so the query targets yogurt products specifically. I also used `sort_by=last_modified_t` and `page_size=10` to return one small, recent page of yogurt items.

The script makes an HTTP request with Python (`urllib.request`), parses the JSON response (`json.loads`), and extracts yogurt-related product fields into a clean table. For each returned yogurt item, I extract:
- `code` (barcode)
- `product_name`
- `nutrition_grades` (Nutri-Score letter)
- `categories_tags_en` (used to derive a readable yogurt category leaf)

This produced yogurt records such as **"Key Lime Flavored Yogurt"**, **"Greek Style Thick & Creamy Natural Yogurt"**, and **"Greek Yogurt Vanilla"** in `openfoodfacts_search_sample.csv`. I print these yogurt results in the terminal and save the same rows to CSV for analysis.

Read-only search on Open Food Facts does not require an API key. I still included `.gitignore` with `.env` in this folder so any future API secret (loaded with `os.environ.get(...)`) stays out of version control, which demonstrates safe credential handling.