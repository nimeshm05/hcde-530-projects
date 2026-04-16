# responses_clean.py

## Purpose

Reads `responses.csv` (same directory as this script), removes rows where `name` is blank (after stripping whitespace), uppercases every value in the `role` column, and writes the result to `responses_cleaned.csv`. After writing, it prints how many **kept** rows look like **UX designers**, **UX researchers**, and **product managers** (using simple keyword rules on the uppercased `role` string).

## Inputs / dependencies

- **`responses.csv`** next to this script (`Path(__file__).parent`).
- Standard library: `csv`, `pathlib`.

## How to run

From `week-3/`:

```bash
python3 responses_clean.py
```

From the repo root:

```bash
python3 week-3/responses_clean.py
```

## Outputs

- **`responses_cleaned.csv`**: same columns and order as the input header; only rows with a non-empty `name`; `role` values are stripped then uppercased.
- Terminal summary: rows read, kept, dropped; then counts for UX designers, UX researchers, and product managers among kept rows.
