# demo_responses.csv

## Purpose

Sample participant responses for the word-count demo (`demo_word_count.py`).

## Format

- Header: `participant_id`, `role`, `response`
- `response` values may be quoted when they contain commas.

## How to use

Read with `csv.DictReader`; word-count logic uses the `response` column.

## Related files

- **`demo_word_count.py`** — loads this file and prints per-row and aggregate word statistics.
