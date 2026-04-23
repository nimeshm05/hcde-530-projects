# `fetch_reviews.md`

## Purpose

Download review data from the week-4 class API and extract each review’s **research category** and **helpful vote** count for inspection and CSV export.

## Inputs / dependencies

- Network access to `https://hcde530-week4-api.onrender.com/reviews/`
- Python 3.10+ (uses `list[dict]` type hints)
- If you see an SSL certificate error on macOS, install CA bundles: `pip install certifi` (the script uses `certifi` when it is installed)

## How to run

From this directory:

```bash
python3 fetch_reviews.py
```

## Outputs

- **Stdout:** one line per review: `category: N helpful votes`, then a line noting the top-50 file
- **`reviews_category_helpful_votes.csv`** in the same folder, with columns `category` and `helpful_votes` (all reviews)
- **`reviews_top50_helpful_votes.csv`** — the 50 rows with highest `helpful_votes` (see `reviews_top50_helpful_votes.md`)
