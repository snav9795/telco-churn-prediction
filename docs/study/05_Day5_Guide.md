# Day 5 — Streamlit web app (local)

**CS5998 Capstone Project | ~2 hours**

**Output:** `churn-prediction/app/` with a runnable multi-page Streamlit app: live prediction, dashboard, bulk CSV.

---

## 1. Concepts

- **Streamlit:** Reruns the script on interaction; use `st.session_state` for heavy loads (model, explainer) so you do not reload every click.
- **Multipage app:** Either `pages/` folder (`streamlit run app/Home.py`) or `st.navigation` (newer API)—pick one; official docs recommend `pages/` for simplicity.
- **Inference:** Load saved model + preprocessor; build the same feature vector as training from widgets or uploaded CSV.

---

## 2. Why it matters

Demonstrates **end-to-end system** beyond notebooks—strong alignment with professionalism and deployment story (Day 6).

---

## 3. Suggested folder layout

```
churn-prediction/
├── app/
│   ├── Home.py                 # entry: streamlit run app/Home.py
│   ├── pages/
│   │   ├── 1_Predict.py
│   │   ├── 2_Dashboard.py
│   │   └── 3_Bulk.py
│   └── utils.py                # load_model(), preprocess_input(), optional
├── models/
│   └── ... saved artifacts
```

Add to `requirements.txt`: `streamlit`, `shap`, `plotly` (optional for charts).

Run locally:

```bash
cd churn-prediction
venv\Scripts\activate
streamlit run app/Home.py
```

---

## 4. Page specifications

### Page 1 — Live prediction

- **Sidebar:** Inputs for each raw feature (sliders, selects) matching training columns—or a subset with sensible defaults.
- **Button:** “Predict churn”.
- **Output:** Predicted probability, label High/Medium/Low risk (pick thresholds, document them).
- **Optional:** SHAP waterfall for that synthetic row (same feature order as model input).

**Implementation tip:** Build a `pandas.DataFrame` with one row in the **exact** column order the pipeline expects.

### Page 2 — Model dashboard

- Confusion matrix (test set), ROC curve, metric cards (precision, recall, F1, accuracy, ROC-AUC).
- Feature importance or mean |SHAP| bar chart.
- Small table comparing Logistic Regression vs XGBoost metrics (from Day 3).

Use cached `@st.cache_resource` for model loads:

```python
import streamlit as st

@st.cache_resource
def load_artifacts():
    # joblib.load preprocessor + model
    return preprocessor, model
```

### Page 3 — Bulk prediction

- `st.file_uploader` for CSV.
- Apply same preprocessing as training; `predict_proba`.
- `st.dataframe` results + `st.download_button` for CSV export.

---

## 5. What “done” looks like

- All three pages reachable from sidebar without errors.
- No hardcoded absolute paths: use `Path(__file__).parent.parent` to resolve `models/` relative to `churn-prediction/`.

---

## 6. Viva prep

1. **Why Streamlit?** Fast ML UI in pure Python; good for capstone demos.
2. **How do you ensure training–serving consistency?** Same saved pipeline/preprocessor and column order.
3. **What fails if CSV columns differ?** Preprocessor should `handle_unknown='ignore'` or validate columns up front.

---

**Previous:** [`04_Day4_Guide.md`](04_Day4_Guide.md) · **Next:** [`06_Day6_Guide.md`](06_Day6_Guide.md)
