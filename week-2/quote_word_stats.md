# quote_word_stats.py

## Purpose

Reads literary quotes from `quotes.csv`, counts words per quote, lists each author’s count, and prints shortest, longest, and average word counts (with author names for min/max).

## Inputs / dependencies

- **`quotes.csv`** in the same directory as this script (resolved via `Path(__file__).parent`).
- Standard library: `csv`, `pathlib`.

## How to run

From `week-2/`:

```bash
python3 quote_word_stats.py
```

Or from the repo root:

```bash
python3 week-2/quote_word_stats.py
```

## Outputs

- Text to stdout: per-author word counts, then a summary (shortest, longest, average).
