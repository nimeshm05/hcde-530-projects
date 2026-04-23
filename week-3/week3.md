# Week 3: Competency 3 — Data Cleaning and File Handling

I used Cursor to step through **week3_analysis_buggy.py**, identifying potential issues and iterating on fixes. Cursor agent did a very good job in identifying the following underlying issues:

1. Crash (confirmed): ValueError: invalid literal for int() with base 10: 'fifteen'
2. Data-quality issue (not crashing): one row has empty role (R005), so role counting includes a blank key (": 1" in output).
3. Logic bug (would appear after crash is fixed): “Top 5 highest satisfaction scores” is implemented as ascending sort + first 5

After identifying the issues, I asked Cursor agent to suggest potential solutions to the underlying issues. Here are my claims:

1. Issue 1: Cursor did good job in recommending a try/except block to prevent the script from crashing on dirty numeric fields (like experience_years = "fifteen" in the CSV file). However, it did not report why it skipped the dirty numeric fields. This is an issue because when a codefile is shared among multiple people, it can be challenging for collaborators to understand the statement logic. In order to overcome this issue, I created a list that collects row IDs and prints the summaries when the crash occurs. 
**For ex: Skipped rows with invalid experience_years: 1 (R009)**

2. Issue 3: In order to overcome the logic issue, I ideated potential fixes with cursor agent and modified the codefile to include the following:
`scored_rows.sort(key=lambda x: x[1], reverse=True)` 
`top5 = scored_rows[:5]`
The output now prints the correct data - top 5 highest satisfaction scores instead of bottom 5.