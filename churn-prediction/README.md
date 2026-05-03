# Telco Customer Churn Prediction

**CS5998 Capstone Project | Master of Data Science & Artificial Intelligence**

## Live Demo

> **[Launch the Streamlit app →](https://telco-churn-prediction.streamlit.app)**  
> Hosted on [Streamlit Community Cloud](https://share.streamlit.io) from the public repo [`snav9795/telco-churn-prediction`](https://github.com/snav9795/telco-churn-prediction).  
> *Free-tier apps sleep after inactivity — allow ~30 s for a cold start.*

## Project Overview

This project implements an end-to-end machine learning pipeline to predict customer churn for a telecommunications company. The goal is to identify customers likely to cancel their service, enabling proactive retention strategies.

### Project Scope

| Dimension | Choice |
|-----------|--------|
| **Problem Type** | Binary Classification (Will customer churn? Yes/No) |
| **Data Type** | Tabular |
| **Technique Category** | Machine Learning |
| **System Context** | Prediction Pipeline + Interpretation Dashboard |

## Dataset

**Source:** [Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

- **Records:** 7,043 customers
- **Features:** 21 (demographics, services, account info)
- **Target:** Churn (Yes/No)

## Repository context

This directory is the **Python project** inside the capstone workspace. Course documents, study guides, and formal submissions live under `../docs/` at the repository root (see the root `README.md`).

## Project Structure

```
churn-prediction/
├── app/
│   ├── Home.py                 # Streamlit entry point
│   ├── utils.py                # Shared artifact loader
│   └── pages/
│       ├── 1_Predict.py        # Single-customer prediction + SHAP
│       ├── 2_Dashboard.py      # Model comparison dashboard
│       └── 3_Bulk.py           # Batch CSV scoring
├── data/
│   ├── raw/                    # Original dataset
│   └── processed/              # train.csv / test.csv
├── models/                     # preprocessor.joblib, logistic_regression.joblib, xgboost.joblib
├── notebooks/
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb  # Data preprocessing pipeline
│   ├── 03_modeling.ipynb       # Model training & evaluation
│   └── 04_interpretation.ipynb # SHAP interpretation
├── reports/
│   └── figures/                # SHAP plots, architecture diagram
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation & Local Run

```bash
# Clone the public repo (or navigate to churn-prediction/ in the full workspace)
git clone https://github.com/snav9795/telco-churn-prediction.git
cd telco-churn-prediction

# Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/Home.py
```

The app will open at `http://localhost:8501`.

## Deployment (Streamlit Community Cloud)

1. Push `churn-prediction/` content to the public repo root (already configured via `git subtree push`).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Select repo `snav9795/telco-churn-prediction`, branch `main`, main file `app/Home.py`.
4. Choose Python 3.11 (matches local environment).
5. Click **Deploy** — the app URL will be `https://telco-churn-prediction.streamlit.app`.

## Reproducibility Checklist

- [x] `requirements.txt` installs cleanly in a fresh venv
- [x] `random_state=42` used for train/test split and all models
- [x] Raw data path documented (`data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`)
- [x] Notebooks run top-to-bottom in order: `01_eda` → `02_preprocessing` → `03_modeling` → `04_interpretation`
- [x] Streamlit run command: `streamlit run app/Home.py`
- [x] Public app URL: <https://telco-churn-prediction.streamlit.app>

## Milestones

- [x] **Milestone 1:** Project Definition (Week 4)
- [ ] **Milestone 2:** Technical Checkpoint (Week 8)
- [ ] **Milestone 3:** Final Submission (Week 12)

## Methods

1. **Baseline Model:** Logistic Regression
2. **Improved Model:** XGBoost / Random Forest with hyperparameter tuning
3. **Interpretation:** SHAP values for model explainability

## Author

Student - Master of Data Science & Artificial Intelligence

---

*Project created: February 2026*
