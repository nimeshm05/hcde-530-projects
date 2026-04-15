# demo_word_count.py

## Purpose

Demo script that loads participant responses from a CSV, counts words in each `response` field, prints a per-row table, then prints summary statistics (count, shortest, longest, average).

## Inputs / dependencies

- **`demo_responses.csv`** in the working directory (same folder as the script when run from `week-2`).
- Standard library: `csv`.

## How to run

From `week-2/`:

```bash
python3 demo_word_count.py
```

## Outputs

- Text to stdout: table with `participant_id`, `role`, word count, and a truncated response preview; then a short summary block.
