# C6 Competency Claim — Data Visualization

I built charts in Python that answer specific analytical questions, chose chart types that match the shape of the data and the argument I wanted to make, and documented the analysis in a Jupyter notebook so someone else can run the code, see the outputs, and follow the reasoning in markdown cells.

**Evidence I am claiming:**

- Charts are generated in Python with Plotly (`plotly.express`), which satisfies the same intent as matplotlib, seaborn, or pandas plotting: programmatic, reproducible figures tied to the analysis code.
- For each analytical question below, I state why that chart type fits the data and the question.
- The full artifact is the notebook `**openfoodfacts_cereals_visualisation.ipynb`** in this repo.

---

## Analytical question 1

Among breakfast cereals in the database, which brands have the highest average sugar content per 100 g, and does a product’s Nutri-Score (A–E) reliably rank with its actual sugar level?

**Competency claim:** 

I used a **horizontal bar chart** (mean sugar by brand) because I had **many brand names** and needed to **compare magnitudes on a common scale**; horizontal layout keeps long brand strings readable; vertical bars with rotated labels would be harder to scan. I used a **box plot** of sugar by Nutri-Score letter because the question is about **distribution and overlap**, not just averages: boxes show median, spread, and outliers per grade so readers can judge whether worse letters align with higher sugar while seeing variability. I added a **line chart of mean sugar by grade** as a compact summary of the same ordinal relationship, and a **Spearman correlation** printed from the notebook to quantify how strongly the grade ordering tracks sugar. Those figures and the filtering rules (e.g. excluding unknown grades, minimum products per brand) are implemented and explained in the notebook linked above.

---

## Analytical question 2

What share of products that include health-oriented keywords (“whole grain,” “natural,” “fiber”) in the product name have a Nutri-Score of C or worse?

**Competency claim:** 

I used a **donut (pie) chart** because the outcome is a **single population split into two parts** (among keyword-matching products with a known A–E score: C–E vs A–B). A part-to-whole share is what pie-style charts encode well; the donut keeps the center usable for emphasis and the trace shows **percent, label, and raw count** so the argument is not only proportional but countable. I paired it with **printout of counts and percentages** in the code output so a reader can verify the headline without reading numbers only off the curve. The logic (regex on `product_name`, definition of C or worse, exclusion of unknown grades) lives in the same notebook section with markdown context.

---

## Analytical question 3

Which nutritional fields (e.g., fiber, salt, saturated fat, energy) are most frequently missing across products in this category, and does data completeness vary by country of origin?

**Competency claim:** 

I used a **horizontal bar chart** of **percent missing by field** because I needed a **direct ranking** of which columns are weakest dataset-wide—bars make “most missing” versus “least missing” immediate without comparing many numbers in a table. I used a **heatmap** (country × field, colored by percent missing) because the question has **two categorical dimensions** (normalized country and nutrient field) and one **continuous measure** (missing rate); a heatmap lets the eye compare **both** “which fields are bad overall” and **whether some countries are systematically sparser** than others, which a single aggregate chart would not show. Country groups are restricted to places with enough rows so the grid is not dominated by noise. Again, code, charts, and narrative sit in the Jupyter notebook at the link above.

---

