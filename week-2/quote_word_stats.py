import csv
from pathlib import Path


def count_words(text: str) -> int:
    return len(text.split())


def main() -> None:
    # code that finds the csv file and reads it
    csv_path = Path(__file__).resolve().parent / "quotes.csv"

    # code that defines a list of tuples to store the results
    rows: list[tuple[str, int]] = []

    # code that reads the csv file and stores the results in a list of tuples
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append((row["author"], count_words(row["quote"])))

    counts = [c for _, c in rows]
    shortest = min(counts)
    longest = max(counts)
    average = sum(counts) / len(counts)

    short_authors = [a for a, c in rows if c == shortest]
    long_authors = [a for a, c in rows if c == longest]

    print("Quote word counts")
    print("-" * 40)

    # code that prints the words in the csv file and the author name
    for author, n in rows:
        print(f"  {n:2}  {author}")
    print()
    print("Summary")
    print("-" * 40)
    print(f"  Shortest : {shortest} words ({', '.join(short_authors)})")
    print(f"  Longest  : {longest} words ({', '.join(long_authors)})")
    print(f"  Average  : {average:.1f} words")


if __name__ == "__main__":
    main()
