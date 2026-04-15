# quotes.csv

## Purpose

Small dataset of quotes for exercises (e.g. word-count stats in `quote_word_stats.py`).

## Format

- Header: `author`, `quote`
- One row per quote; the `quote` field may be quoted in CSV when it contains commas.

## How to use

Read with `csv.DictReader`; use the `quote` column for text analysis and `author` for labels.

## Related files

- **`quote_word_stats.py`** — word counts and summary stats for this file.
