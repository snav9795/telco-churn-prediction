# Telco Customer Churn Prediction

**CS5998 Capstone Project | Master of Data Science & Artificial Intelligence**

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
├── data/
│   ├── raw/                    # Original dataset
│   └── processed/              # Cleaned & transformed data
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb  # Data preprocessing
│   ├── 03_baseline_model.ipynb # Logistic Regression baseline
│   └── 04_improved_model.ipynb # XGBoost/Random Forest
├── src/
│   ├── data_preprocessing.py   # Data cleaning functions
│   ├── feature_engineering.py  # Feature transformation
│   ├── model_training.py       # Model training utilities
│   └── evaluation.py           # Evaluation metrics
├── models/                     # Saved trained models
├── reports/                    # Generated reports & figures
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation

```bash
# Clone or navigate to project directory
cd churn-prediction

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

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
