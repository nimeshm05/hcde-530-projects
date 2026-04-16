# week3_analysis_buggy.py

## Purpose

Loads messy survey rows from `week3_survey_messy.csv`, prints role counts, average years of experience (skipping non-numeric values), the five highest satisfaction scores, then three extra summaries: by department, by primary tool, and low-satisfaction alerts.

## Inputs / dependencies

- **`week3_survey_messy.csv`** in the working directory (same pattern as the script’s `filename` string).
- Standard library: `csv`.

## How to run

From `week-3/` (so the CSV path resolves):

```bash
python3 week3_analysis_buggy.py
```

## Outputs

Printed to the terminal:

- Responses by role (normalized with `.title()`).
- Average years of experience, or `N/A` if no valid integers.
- Top 5 satisfaction scores (highest first).
- **Responses by department** — from `print_department_breakdown`.
- **Responses by primary tool** — from `print_primary_tool_counts`.
- **Low satisfaction alerts** — rows with score ≤ 2 (`print_low_satisfaction_alerts`); `(none found)` if no matches.
