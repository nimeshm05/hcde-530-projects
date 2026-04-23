import csv


def print_department_breakdown(rows):
    """Print how many responses fall under each department (stdout).

    ``rows`` is a list of row dicts from ``csv.DictReader`` on ``week3_survey_messy.csv``.
    For each row, reads ``department``: strips whitespace and applies ``.title()`` so
    values like ``DESIGN`` and ``Design`` merge. Prints a header, then one line per
    department in alphabetical order: ``  <Department>: <count>``. Rows with a
    missing or empty department are counted under an empty label (after strip/title).
    """
    counts = {}
    for row in rows:
        dept = (row.get("department") or "").strip().title()
        counts[dept] = counts.get(dept, 0) + 1

    print("\nResponses by department:")
    for dept, count in sorted(counts.items()):
        print(f"  {dept}: {count}")


def print_primary_tool_counts(rows):
    """Print how many respondents named each primary tool (stdout).

    ``rows`` is a list of row dicts from ``csv.DictReader``. Reads ``primary_tool``,
    strips and ``.title()`` so ``figma`` and ``Figma`` count together. Prints a header
    then one line per tool sorted alphabetically: ``  <Tool>: <count>``. Empty
    tools are grouped under an empty label.
    """
    counts = {}
    for row in rows:
        tool = (row.get("primary_tool") or "").strip().title()
        counts[tool] = counts.get(tool, 0) + 1

    print("\nResponses by primary tool:")
    for tool, count in sorted(counts.items()):
        print(f"  {tool}: {count}")


def print_low_satisfaction_alerts(rows, threshold=2):
    """Print survey rows whose satisfaction score is at or below a threshold (stdout).

    ``rows`` is a list of row dicts. Reads ``satisfaction_score``; if it is empty after
    strip, the row is skipped. If the value is not a valid integer, the row is skipped
    (no crash). For integer scores ``<= threshold`` (default ``2``), prints one line
    with ``response_id``, ``participant_name``, and score. Prints a section header first;
    if no rows qualify, prints ``(none found)`` on one line.
    """
    print(f"\nLow satisfaction alerts (score <= {threshold}):")
    found = False
    for row in rows:
        raw = (row.get("satisfaction_score") or "").strip()
        if not raw:
            continue
        try:
            score = int(raw)
        except ValueError:
            continue
        if score <= threshold:
            found = True
            rid = (row.get("response_id") or "").strip()
            name = (row.get("participant_name") or "").strip()
            print(f"  {rid} | {name} | {score}")
    if not found:
        print("  (none found)")


# Load the survey data from a CSV file
filename = "week3_survey_messy.csv"
rows = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Count responses by role
# Normalize role names so "ux researcher" and "UX Researcher" are counted together
role_counts = {}

for row in rows:
    role = row["role"].strip().title()
    if role in role_counts:
        role_counts[role] += 1
    else:
        role_counts[role] = 1

print("Responses by role:")
for role, count in sorted(role_counts.items()):
    print(f"  {role}: {count}")

# Calculate the average years of experience
total_experience = 0
valid_experience_rows = 0
invalid_experience_ids = []
for row in rows:
    try:
        total_experience += int(row["experience_years"])
        valid_experience_rows += 1
    # skip rows with invalid experience values
    except (TypeError, ValueError):
        invalid_experience_ids.append((row.get("response_id") or "").strip())
        continue

if valid_experience_rows:
    avg_experience = total_experience / valid_experience_rows
    print(f"\nAverage years of experience: {avg_experience:.1f}")
else:
    print("\nAverage years of experience: N/A (no valid numeric values)")
if invalid_experience_ids:
    print(
        "Skipped rows with invalid experience_years: "
        f"{len(invalid_experience_ids)} ({', '.join(invalid_experience_ids)})"
    )

# Find the top 5 highest satisfaction scores
scored_rows = []
invalid_score_ids = []
for row in rows:
    if row["satisfaction_score"].strip():
        try:
            scored_rows.append((row["participant_name"], int(row["satisfaction_score"])))
        except ValueError:
            # Skip rows with invalid satisfaction score and add the row ID to the list to be printed later
            invalid_score_ids.append((row.get("response_id") or "").strip())

# Sort the scored rows by satisfaction score in descending order (highest to lowest) - Corrected the logic issue of showing the bottom 5 satisfaction scores instead of the top 5
scored_rows.sort(key=lambda x: x[1], reverse=True)
top5 = scored_rows[:5]

print("\nTop 5 satisfaction scores:")
for name, score in top5:
    print(f"  {name}: {score}")
if invalid_score_ids:
    print(
        "Skipped rows with invalid satisfaction_score: "
        f"{len(invalid_score_ids)} ({', '.join(invalid_score_ids)})"
    )

print_department_breakdown(rows)
print_primary_tool_counts(rows)
print_low_satisfaction_alerts(rows)
