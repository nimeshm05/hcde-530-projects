# responses.csv

## Purpose

Sample **job roster** data for testing [`responses_clean.py`](responses_clean.py): names, job `role`, `years_experience`, and `responsibilities`. Most rows are UX designers, UX researchers, or product managers; a few rows use other titles. Two rows have blank names so the cleaner can drop them.

## Inputs / dependencies

None (static data file). UTF-8 CSV with header: `name`, `role`, `years_experience`, `responsibilities`.

## How to run or use

Place this file in `week-3/` (next to `responses_clean.py`), then run:

```bash
python3 week-3/responses_clean.py
```

Or from `week-3/`:

```bash
python3 responses_clean.py
```

## Outputs

None from this file directly. Running the cleaner produces `responses_cleaned.csv` in the same folder.
