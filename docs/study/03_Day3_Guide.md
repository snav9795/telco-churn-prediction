# Day 3 — Baseline & improved models

**CS5998 Capstone Project | ~2 hours**

**Output:** Trained Logistic Regression and XGBoost (or similar), metrics table, model files in `churn-prediction/models/`.

---

## 1. Concepts

- **Logistic regression:** Linear decision boundary; outputs probabilities via sigmoid; fast, interpretable baseline.
- **XGBoost:** Gradient boosted trees; captures non-linearities and interactions.
- **Hyperparameters:** e.g. `max_depth`, `learning_rate`, `n_estimators` for XGBoost—tune with validation or small grid search.
- **Metrics:** Accuracy, precision, recall, F1, ROC-AUC; confusion matrix. For churn, **recall** (catching churners) often matters to the business.
- **Imbalanced data:** Compare ROC-AUC and PR-AUC; consider class weights or scale_pos_weight in XGBoost.

---

## 2. Why it matters

Milestone 2 requires **working models** and **comparison**. A table beats prose.

---

## 3. Step-by-step tasks

1. Notebook `03_modeling.ipynb` (or split baseline vs tuned).
2. Load **preprocessed** train/test from Day 2—or rebuild pipeline from saved preprocessor.
3. **Logistic regression:** `sklearn.linear_model.LogisticRegression` with `class_weight='balanced'` optional; `max_iter` high enough to converge.
4. **Train** on training set; **predict** and **predict_proba** on test.
5. **XGBoost:** `xgboost.XGBClassifier`; use `eval_metric='logloss'`, set `random_state`; consider `scale_pos_weight = neg/pos` count ratio.
6. Compute for **both** models on test: accuracy, precision, recall, F1, ROC-AUC; confusion matrices.
7. Optional: 5-fold CV on train for XGBoost hyperparameters (keep test untouched).
8. **Save models:** `joblib.dump(model, 'models/logistic_regression.joblib')` etc.; save feature names list if needed for SHAP.

---

## 4. Reading the outputs

- If LR and XGBoost are close, XGBoost may still win on ROC-AUC or recall.
- High accuracy + low recall on churn → classic imbalance symptom.
- Use **probability threshold** discussion in report (default 0.5 may not be optimal for the business).

---

## 5. Viva prep

1. **Why start with logistic regression?** Simple, fast baseline; interpretable coefficients.
2. **What does XGBoost add?** Non-linear splits, feature interactions.
3. **Which metric do you care about most and why?** Tie to cost of missing a churner vs false alarm.

---

**Previous:** [`02_Day2_Guide.md`](02_Day2_Guide.md) · **Next:** [`04_Day4_Guide.md`](04_Day4_Guide.md)
