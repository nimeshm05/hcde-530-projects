# week3_survey_clean.py

## Purpose

Reads [`week3_survey_messy.csv`](week3_survey_messy.csv), applies light cleaning, and writes [`week3_survey_cleaned.csv`](week3_survey_cleaned.csv) in the same folder.

## Cleaning rules

- Strip whitespace on every column.
- **Drop** rows where `participant_name` is empty after stripping.
- **`role`**, **`department`**, **`primary_tool`:** non-empty values are normalized with `.title()` (e.g. `DESIGN` → `Design`, `figma` → `Figma`).
- **`experience_years`** and **`satisfaction_score`:** if the value is a valid integer string, it is rewritten as a plain integer string; otherwise the cell is written **empty** (e.g. `fifteen` becomes blank).

## Inputs / dependencies

- **`week3_survey_messy.csv`** next to this script (`Path(__file__).parent`).
- Standard library: `csv`, `pathlib`.

## How to run

From `week-3/`:

```bash
python3 week3_survey_clean.py
```

From the repo root:

```bash
python3 week-3/week3_survey_clean.py
```

## Outputs

- **`week3_survey_cleaned.csv`:** same columns and order as the input header.
- A short summary is printed (rows read, written, dropped).
