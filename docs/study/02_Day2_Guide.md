# Day 2 — Preprocessing & train/test split

**CS5998 Capstone Project | ~2 hours**

**Output:** Cleaned dataset saved under `churn-prediction/data/processed/`, reproducible preprocessing notebook.

---

## 1. Concepts

- **Encoding:** Models need numbers; categories become one-hot columns (or binary flags).
- **Imputation:** Replace missing `TotalCharges` sensibly (e.g. 0 if tenure is 0, or median).
- **Scaling:** Standardize numeric features so linear models treat scales fairly (often `StandardScaler`).
- **Train/test split:** Train only on training data; test simulates new customers.
- **Stratify:** Use `stratify=y` so churn rate matches in train and test.
- **Leakage:** Do not use test statistics to choose imputation or scaling—`fit` scaler on train only, `transform` both.

---

## 2. Why it matters

Bad preprocessing = inflated scores or models that fail in production. Milestone 2 rewards **correct methodology**.

---

## 3. Step-by-step tasks

1. Copy ideas into `02_preprocessing.ipynb` (or extend Day 1 notebook—prefer separate for clarity).
2. Load raw CSV; drop or fix `customerID`-like columns if they are pure identifiers (no predictive value, risk of leakage of identity).
3. Separate **X** and **y** (`Churn` → 0/1).
4. **Impute** `TotalCharges` for the 11 missing rows (document rule in a markdown cell).
5. **Split:** e.g. 80/20, `random_state=42`, stratified.
6. **Column types:** List categorical vs numeric columns.
7. **Pipeline approach (recommended):** `ColumnTransformer` with:
   - One-hot (or `OneHotEncoder(handle_unknown='ignore')`) for categoricals
   - `StandardScaler` for numerics
8. **`fit_transform` on train**, **`transform` on test** only.
9. Save **processed** arrays or a parquet of the transformed training frame if you need traceability—or save the **fitted preprocessor** with `joblib` for the app later.
10. Write `data/processed/` artifact: e.g. `train.csv` / `test.csv` **after** encoding *or* save numpy + preprocessor; pick one strategy and stay consistent through Day 3.

**Consistency tip:** Many students keep a single `preprocess.py` or sklearn `Pipeline` object saved to `models/preprocessor.joblib` so the Streamlit app reuses the exact same steps.

---

## 4. Reading the outputs

- Train and test should have **similar** churn proportions.
- Feature count after one-hot will be larger than raw columns—normal.
- If test accuracy later is weird, first suspect **leakage** or **double-fitting** on full data.

---

## 5. Viva prep

1. **Why one-hot vs label encoding?** Nominal categories have no order; one-hot avoids fake ordering.
2. **Why fit scaler on train only?** Test must mimic unseen future data.
3. **What is stratification?** Preserves class balance in both splits.

---

**Previous:** [`01_Day1_Guide.md`](01_Day1_Guide.md) · **Next:** [`03_Day3_Guide.md`](03_Day3_Guide.md)
