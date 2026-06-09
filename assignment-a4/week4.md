# C4 — APIs and Data Acquisition

I met this competency with `openfoodfacts_search.py` in this folder by building a **yogurt-focused API workflow**. I used the Open Food Facts v2 search endpoint (`GET https://world.openfoodfacts.org/api/v2/search`) and set `categories_tags_en=Yogurt` so the query targets yogurt products specifically. I also used `sort_by=last_modified_t` and `page_size=10` to return one small, recent page of yogurt items.

The script makes an HTTP request with Python (`urllib.request`), parses the JSON response (`json.loads`), and extracts yogurt-related product fields into a clean table. For each returned yogurt item, I extract:
- `code` (barcode)
- `product_name`
- `nutrition_grades` (Nutri-Score letter)
- `categories_tags_en` (used to derive a readable yogurt category leaf)

This produced yogurt records such as **"Key Lime Flavored Yogurt"**, **"Greek Style Thick & Creamy Natural Yogurt"**, and **"Greek Yogurt Vanilla"** in `openfoodfacts_search_sample.csv`. I print these yogurt results in the terminal and save the same rows to CSV for analysis.

Read-only search on Open Food Facts does not require an API key. I still included `.gitignore` with `.env` in this folder so any future API secret (loaded with `os.environ.get(...)`) stays out of version control, which demonstrates safe credential handling.

---

## A4 — Independent API workflow

For A4 I repeated the class pattern on my own: I chose the API, picked data I care about, and documented the full workflow in this folder (`openfoodfacts_search.py`, `openfoodfacts_search_sample.csv`, and this file).

### API and data I chose

- **API:** [Open Food Facts](https://world.openfoodfacts.org/) v2 search (`GET /api/v2/search`) — a public, crowd-sourced food database.
- **Data focus:** **yogurt** products, filtered with `categories_tags_en=Yogurt`, because I often compare labels in the grocery aisle and wanted real product names, barcodes, categories, and Nutri-Score letters in one pull.
- **Why this API:** It is free for read-only search, returns structured JSON, and maps directly to everyday food-labeling decisions — not a toy dataset.

### What I did (end to end)

1. Defined query parameters (category, sort, field subset, page size) so the response stayed small and relevant.
2. Called the API with Python (`urllib.request`), handled transient server errors with retries, and parsed JSON.
3. Extracted four fields per product (`code`, `product_name`, `nutrition_grades`, category leaf) into a readable table.
4. Printed results for quick inspection and saved the same rows to `openfoodfacts_search_sample.csv` for later analysis (A5/A6 build on related food data).

### Why this matters for HCD work

Human-centered design often starts with **understanding how people make choices with incomplete or uneven information**. Grocery shopping is a clear example: someone may scan a shelf of yogurts and rely on product names, category wording (“Greek-style,” “protein,” “organic”), and summary grades — not full nutrition panels.

This workflow mirrors how an HCD team might **acquire external data** before interviews or prototyping:

- **Scoping a real domain:** Yogurt is a bounded category with meaningful variation (Greek-style, flavored drinks, fruit/sugar blends) — similar to scoping a user problem before building a solution.
- **Working with messy, real-world records:** Names are inconsistent (“Greek Yogurt Vanilla” vs. “Greek Style Thick & Creamy Natural Yogurt”), grades are sometimes missing, and categories use internal tags. That is the kind of inconsistency designers and researchers see in production data, not in clean classroom CSVs.
- **Separating signal from noise:** Limiting `fields` and deriving a single `category_leaf_en` is a small version of **data shaping for downstream use** — the same discipline needed before charts, filters, or UI that must not overwhelm users.
- **Reproducible evidence:** Saving CSV output and scripting the request means another researcher can rerun the pull, compare a new sample, or audit what was shown in a prototype backed by live product data.
- **Ethical and practical constraints:** Using a public read API, keeping secrets out of git (`.gitignore`), and requesting only what is needed reflects responsible practice when connecting user-facing experiences to third-party data.

In short, A4 is not only “call an API.” It practices the HCD-relevant habit of **turning an open data source about everyday behavior into structured, inspectable evidence** you can use to ask better questions — e.g., whether “health” wording in product names aligns with Nutri-Score, or whether certain yogurt subcategories are under-labeled — before designing interfaces that help people choose with more confidence.