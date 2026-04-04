# Day 1 — EDA & project setup

**CS5998 Capstone Project | ~2 hours**

**Output:** Environment ready, first EDA notebook with churn rate, distributions, correlation heatmap, missing-value check.

---

## 1. Concepts

- **Machine learning:** Learn patterns from data to predict churn for new customers.
- **Binary classification:** Target is two classes: Churn Yes / No.
- **EDA:** Explore distributions, relationships, and data quality before modeling.
- **Class imbalance:** If ~27% churn, accuracy alone can look “good” while ignoring churners—note this today for later metrics.

---

## 2. Why it matters

Milestone 2 expects evidence you **understand the data**. Clear EDA figures become figures in your report and support every modeling choice later.

---

## 3. Step-by-step tasks

### 3.1 Milestone 1 (if not done)

1. Open [`churn-prediction/reports/Milestone_1_Project_Definition.md`](../../churn-prediction/reports/Milestone_1_Project_Definition.md) (or your portal submission).
2. Add your name, dates, and any course-specific fields; submit per LMS instructions.

### 3.2 Environment

From the **repository root**:

```bash
cd churn-prediction
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Add notebook stack if missing: `pip install jupyter ipykernel pandas matplotlib seaborn`.

### 3.3 EDA notebook

1. Create `churn-prediction/notebooks/` if needed.
2. New notebook, e.g. `01_eda.ipynb`.
3. Load raw data: `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv` (filename may vary slightly).
4. **Churn rate:** bar chart or count plot of `Churn` (Yes/No).
5. **Numeric features:** histograms or KDEs for `tenure`, `MonthlyCharges`, `TotalCharges` (handle the 11 missing `TotalCharges` rows—note them, full fix on Day 2).
6. **Categorical features:** bar charts for `Contract`, `InternetService`, `PaymentMethod`, etc.
7. **Correlation heatmap** for numeric columns.
8. **Missing values:** table of `%` missing per column.

Save the notebook. Export key figures to `churn-prediction/reports/figures/` if you want a tidy report folder.

---

## 4. Reading the outputs

- **Churn bar:** Shows imbalance; drives choice of precision/recall/F1 later.
- **Histograms:** Skewed charges or short tenure may overlap with churn.
- **Heatmap:** Strong correlations suggest redundant features (multicollinearity)—note for modeling.
- **Missing table:** Telco dataset usually has few gaps except `TotalCharges`.

---

## 5. Viva prep

1. **What is churn?** Customers who cancel or stop paying in the observation window.
2. **Why classification?** Discrete outcome Yes/No, not a continuous amount.
3. **Why not only accuracy?** Imbalance lets a naive “always no churn” model look accurate.
4. **What did you learn from EDA in one sentence?** Example: “Churn is ~27%; month-to-month contracts and higher monthly charges associate with higher churn in the plots.”

---

**Next:** [`02_Day2_Guide.md`](02_Day2_Guide.md)
