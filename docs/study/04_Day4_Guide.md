# Day 4 — SHAP & system architecture

**CS5998 Capstone Project | ~2 hours**

**Output:** SHAP plots in `reports/`, architecture diagram (image or draw.io export), interpretation narrative for report.

---

## 1. Concepts

- **Global vs local explanation:** Global = which features matter overall; local = why *this* customer got *this* score.
- **SHAP (SHapley Additive exPlanations):** Fair attribution of how each feature pushes prediction up or down from a baseline.
- **Summary plot:** Each row is a feature; color = feature value; position = SHAP impact on output.
- **Waterfall / force:** For one prediction, step from base value to final log-odds or probability.
- **Model feature importance (tree default):** Often **not** the same as SHAP; SHAP is preferred for consistent comparisons across models when configured correctly.
- **Architecture diagram:** Boxes for data, notebooks, preprocessing, training, model store, app, user—arrows for flow.

---

## 2. Why it matters

Rubric items on **interpretability** and **system vision** are directly supported by SHAP and a clear pipeline diagram.

---

## 3. Step-by-step tasks

### 3.1 SHAP on your best model

1. Notebook `04_interpretation.ipynb`.
2. Use **XGBoost** (or the model you deploy) + test sample (100–500 rows is enough for speed).
3. Install: `pip install shap`.
4. **TreeExplainer** for tree models: `explainer = shap.TreeExplainer(model)` then `shap_values = explainer.shap_values(X_sample)`.
5. For **logistic regression**, use `shap.LinearExplainer` or `KernelExplainer` (slower)—tree path is easier if XGBoost is primary.
6. Generate and save:
   - `shap.summary_plot` → `reports/shap_summary.png`
   - `shap.waterfall_plot` for **3** interesting customers (high risk, low risk, borderline) → `reports/shap_waterfall_1.png` etc.

**Note:** Feature names must align with the matrix passed to SHAP (post-encoding column names).

### 3.2 Architecture diagram

1. Use [draw.io](https://draw.io) or PowerPoint.
2. Include: Raw data → EDA → Preprocessing → Training → Model files → (Streamlit app) → User / business outcome.
3. Export PNG/SVG to `reports/architecture_diagram.png`.

---

## 4. Reading the outputs

- **Summary plot:** Top features are main drivers of churn risk in your model.
- **Waterfall:** Shows whether e.g. “Month-to-month contract” pushes probability up and “long tenure” pushes down.
- **Diagram:** Assessor should trace one path from data to decision without asking you.

---

## 5. Viva prep

1. **What is SHAP in one sentence?** It splits the prediction into contributions per feature vs an average baseline.
2. **Why not only coefficients?** Tree models need SHAP (or similar) for faithful local explanations.
3. **What is the main limitation?** Correlated features can share credit; explanations are model-dependent.

---

**Previous:** [`03_Day3_Guide.md`](03_Day3_Guide.md) · **Next:** [`05_Day5_Guide.md`](05_Day5_Guide.md)
