# C5 Competency Claim — Data Analysis with Pandas

I demonstrated C5 by using pandas to answer three concrete analytical questions on my Open Food Facts breakfast cereals dataset in `assignment-a5/openfoodfacts_cereals_analysis.ipynb`.

For question 1, I grouped cereals by `brands` and computed mean sugar content with `groupby(...).agg(...)`, then evaluated whether Nutri-Score aligns with sugar using grouped means by grade and a Spearman correlation. The results showed a clear gradient in average sugar from grade A (about 5.82 g/100g) to grade E (about 24.98 g/100g), with a positive rank correlation of 0.725, which indicates Nutri-Score generally tracks sugar level in this category.

For question 2, I filtered product names using keyword matching (`whole grain`, `natural`, `fiber`/`fibre`) and computed the share of Nutri-Score C-or-worse items from that subset. Out of 9 keyword-matched products with known grades, 5 were C or worse (55.56%). This suggests that health-oriented wording in names does not reliably indicate stronger nutritional grades.

For question 3, I quantified missing data using `isnull()` and compared completeness across countries with `groupby("countries")` and percentage completeness calculations. Missingness was low overall but not uniform by field (highest for `fiber_100g` at 3.11%), and completeness varied by country labels and sample composition.

Across these analyses, I used multiple pandas operations (`head`, `info`, `value_counts`, boolean filtering, `groupby`, and `isnull`) and wrote interpretations of what the outputs mean for data quality and nutrition patterns, not just what the code does.
