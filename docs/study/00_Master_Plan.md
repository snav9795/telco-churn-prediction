# 00 — Master Plan: 7-Day Churn Prediction Project

**CS5998 Capstone Project | Master of Data Science & Artificial Intelligence**

Read this document first. It maps milestones, daily work, and how the Streamlit web app supports higher rubric bands.

---

## What you are building

A **machine learning system** that predicts telecom customer churn, plus a **browser-based app** (Streamlit) for live prediction, dashboards, and bulk scoring—then **deployed** with a public URL for submissions.

---

## Full pipeline at a glance

```
Raw CSV (7,043 customers)
    → Day 1: EDA (patterns, churn rate, imbalance)
    → Day 2: Preprocessing (encoding, imputation, scaling, train/test split)
    → Day 3: Models (Logistic Regression + XGBoost, metrics)
    → Day 4: SHAP + architecture diagram → reports/
    → Day 5: Streamlit app (3 pages) locally
    → Day 6: GitHub + Streamlit Cloud → live URL
    → Day 7: Final report, demo video, reproducibility checklist
```

---

## Milestones (graded)

| Milestone | Weight | What you submit | Built in |
|-----------|--------|-----------------|----------|
| M1 — Project Definition | 25% | Written definition (scope, data, plan) | Week 1–4 |
| M2 — Technical Checkpoint | 25% | EDA, models, diagram, code link, demo | Days 1–4 (+ app link later) |
| M3 — Final Submission | 50% | Full report, deployed app, reproducibility | Days 5–7 |

---

## Seven-day schedule (about 2 hours per day)

| Day | Focus | Primary output |
|-----|--------|----------------|
| 1 | ML basics, churn problem, EDA | Notebook plots + insights; M1 submitted if required |
| 2 | Preprocessing, leakage, split | `data/processed/` dataset |
| 3 | LR + XGBoost, metrics | Saved models in `models/`, comparison table |
| 4 | SHAP, architecture | Figures in `reports/`, diagram |
| 5 | Streamlit | `churn-prediction/app/` running locally |
| 6 | Git + deploy | GitHub repo + Streamlit Cloud URL |
| 7 | Report + video + checklist | Submission package |

Daily detail: open `01_Day1_Guide.md` … `07_Day7_Guide.md` in this folder.

---

## Why include a web app

Rubric themes such as **end-to-end system vision** and **professionalism** are stronger when assessors can open a **live URL**, run predictions, and see dashboards—not only static notebooks.

---

## Demo video checklist (use on Day 7)

- [ ] State problem and dataset in one sentence
- [ ] Show GitHub repo (structure, README)
- [ ] Open **deployed** app URL (not only localhost)
- [ ] Page 1: one live prediction + risk interpretation
- [ ] Page 2: at least one metric or chart and what it means
- [ ] Page 3: bulk upload or explain capability
- [ ] Mention reproducibility (`requirements.txt`, how to run)
- [ ] Keep to ~6 minutes unless course specifies otherwise

---

## Repository paths (from capstone root)

| Path | Role |
|------|------|
| `churn-prediction/` | Code, data, notebooks, app, models |
| `churn-prediction/data/raw/` | Original CSV |
| `churn-prediction/data/processed/` | Cleaned data after Day 2 |
| `churn-prediction/notebooks/` | EDA, preprocessing, modeling notebooks |
| `churn-prediction/models/` | Saved `.pkl` / `.json` / XGBoost artifacts |
| `churn-prediction/reports/` | Figures, M1 doc, final report draft |
| `churn-prediction/app/` | Streamlit app (Day 5+) |
| `docs/study/` | These guides |

---

## If you fall behind

- **Minimum for a pass:** EDA + one working model + clear metrics (Days 1–3).
- **Target for strong marks:** Add SHAP + diagram (Day 4), then app + deploy (Days 5–6).
- **Glossary:** See `Concepts_Reference.md`.

---

**CS5998 Capstone Project**
