# CS5998 Capstone Project: Project Definition Document

**Student:** Shriram Navaratnalingam
**Program:** Master of Data Science & Artificial Intelligence
**Submission Date:** February 2026

---

## 1. Problem Statement

### 1.1 Business Context

Customer churn—the phenomenon where customers discontinue their service with a company—represents one of the most significant challenges facing telecommunications companies today. Industry research consistently shows that acquiring a new customer costs **5-7 times more** than retaining an existing one, making churn prediction a critical business priority.

For telecommunications providers, where monthly subscription models dominate, even small improvements in customer retention translate to substantial revenue protection. A typical telecom company with 7,000 customers and a monthly churn rate of 26.5% loses approximately 1,850 customers monthly. If the average customer lifetime value exceeds $1,500, this represents millions in potential lost revenue annually.

### 1.2 Problem Definition

This project addresses the binary classification problem:

> **Given a customer's demographic profile, service subscriptions, and account information, can we predict whether they will churn (leave the company) in the near future?**

The prediction task enables:

1. **Proactive Intervention:** Identify at-risk customers before they leave
2. **Resource Optimization:** Target retention efforts efficiently
3. **Business Intelligence:** Understand key drivers of customer attrition

### 1.3 Real-World Relevance

This problem is directly applicable to:

- Telecommunications companies (mobile, internet, cable providers)
- Subscription-based businesses (SaaS, streaming services)
- Financial services (banks, insurance companies)

The methodology developed here transfers to any domain with recurring customer relationships.

---

## 2. Scope Definition via Bounded Choices

| Dimension                    | Choice                                         | Justification                                                                        |
| ---------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Problem Type**       | Binary Classification                          | Churn is a Yes/No outcome; classification is the natural framing                     |
| **Data Type**          | Tabular                                        | Dataset contains structured customer records with categorical and numerical features |
| **Technique Category** | Machine Learning                               | Appropriate for structured data with ~7,000 samples; interpretability is important   |
| **System Context**     | Prediction Pipeline + Interpretation Dashboard | End-to-end system from data ingestion to actionable predictions with explainability  |

---

## 3. Data Source Description

### 3.1 Dataset Overview

**Source:** IBM Sample Data Sets - Telco Customer Churn
**Platform:** [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
**License:** Copyright by authors (open for educational use)

| Attribute                    | Value                                      |
| ---------------------------- | ------------------------------------------ |
| **Total Records**      | 7,043 customers                            |
| **Features**           | 21 columns                                 |
| **Target Variable**    | Churn (Yes/No)                             |
| **Class Distribution** | ~73.5% No Churn, ~26.5% Churn (imbalanced) |
| **Missing Values**     | Minimal (TotalCharges has 11 blank values) |

### 3.2 Feature Categories

| Category               | Features                                                                                                                                | Description                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Demographics** | gender, SeniorCitizen, Partner, Dependents                                                                                              | Customer personal characteristics           |
| **Services**     | PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies | Subscribed services                         |
| **Account**      | tenure, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges                                                         | Relationship and billing information        |
| **Target**       | Churn                                                                                                                                   | Whether customer left within the last month |

### 3.3 Data Quality Assessment

- **Completeness:** 99.8% complete (11 missing TotalCharges values)
- **Consistency:** All categorical values follow expected patterns
- **Timeliness:** Synthetic but realistic business data
- **Appropriateness:** Ideal for classification; sufficient samples for ML techniques

---

## 4. Intended Methods

### 4.1 Technical Approach

The project follows a structured machine learning pipeline:

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Interpretation
```

### 4.2 Methods Linked to Program Modules

| Phase                               | Methods                                                          | Related Module(s)                 |
| ----------------------------------- | ---------------------------------------------------------------- | --------------------------------- |
| **Exploratory Data Analysis** | Descriptive statistics, correlation analysis, distribution plots | Data Analytics, Statistics        |
| **Preprocessing**             | Missing value handling, encoding (one-hot, label), scaling       | Data Engineering, ML Fundamentals |
| **Baseline Model**            | Logistic Regression                                              | Machine Learning                  |
| **Improved Model**            | Random Forest, XGBoost with hyperparameter tuning                | Machine Learning, Advanced ML     |
| **Evaluation**                | Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix | Machine Learning                  |
| **Interpretation**            | SHAP values, feature importance                                  | Explainable AI                    |
| **Class Imbalance**           | SMOTE, class weights, stratified sampling                        | Machine Learning                  |

### 4.3 Model Selection Rationale

| Model                         | Purpose        | Why Selected                                                                 |
| ----------------------------- | -------------- | ---------------------------------------------------------------------------- |
| **Logistic Regression** | Baseline       | Interpretable, fast, strong baseline for binary classification               |
| **Random Forest**       | Improved Model | Handles mixed feature types, robust to outliers, provides feature importance |
| **XGBoost**             | Improved Model | State-of-the-art for tabular data, handles imbalance well                    |

### 4.4 Evaluation Strategy

Given class imbalance (26.5% churn), evaluation will emphasize:

1. **Primary Metrics:**

   - **F1-Score:** Balances precision and recall
   - **ROC-AUC:** Measures discrimination ability across thresholds
   - **Recall (Sensitivity):** Critical for capturing actual churners
2. **Secondary Metrics:**

   - Accuracy, Precision, Specificity
   - Confusion matrix analysis
3. **Validation Approach:**

   - Stratified train-test split (80/20)
   - 5-fold stratified cross-validation

---

## 5. Expected Outputs

### 5.1 Technical Deliverables

| Deliverable                       | Description                                        |
| --------------------------------- | -------------------------------------------------- |
| **Preprocessed Dataset**    | Clean, encoded, scaled data ready for modeling     |
| **Trained Models**          | Saved baseline and improved models (.pkl/.joblib)  |
| **Evaluation Report**       | Comprehensive comparison of model performance      |
| **Interpretation Analysis** | SHAP plots explaining predictions                  |
| **Prediction Pipeline**     | End-to-end code to predict churn for new customers |

### 5.2 Documentation Deliverables

| Deliverable                           | Description                             |
| ------------------------------------- | --------------------------------------- |
| **EDA Notebook**                | Visual exploration of data patterns     |
| **Model Development Notebooks** | Documented training process             |
| **Final Report**                | 25-30 page comprehensive project report |
| **Demo Video**                  | 6-minute walkthrough of the system      |

### 5.3 System Output

For any given customer record, the system will output:

1. **Prediction:** Churn likelihood (Yes/No)
2. **Probability Score:** Confidence level (0-100%)
3. **Explanation:** Top factors driving the prediction (via SHAP)

---

## 6. Key Risks and Assumptions

### 6.1 Risks

| Risk                             | Likelihood | Impact | Mitigation Strategy                                    |
| -------------------------------- | ---------- | ------ | ------------------------------------------------------ |
| **Class Imbalance**        | High       | Medium | Apply SMOTE, class weights, threshold optimization     |
| **Overfitting**            | Medium     | High   | Use cross-validation, regularization, pruning          |
| **Feature Leakage**        | Low        | High   | Careful feature selection, domain knowledge validation |
| **Model Interpretability** | Medium     | Medium | Use SHAP values, keep explainable models               |
| **Generalization**         | Medium     | Medium | Validate on held-out test set, report limitations      |

### 6.2 Assumptions

1. **Data Representativeness:** The dataset adequately represents real-world telecom customer behavior
2. **Feature Stability:** Customer attributes remain relevant predictors over time
3. **Label Quality:** Churn labels are accurate and consistently defined
4. **Independence:** Customer records are independent (no network effects)

### 6.3 Constraints

- **Computational:** Standard laptop/desktop resources (no GPU required)
- **Timeline:** 12-week project timeline with fixed milestones
- **Scope:** No deployment to production; focus on model development and interpretation

---

## 7. Project Timeline

| Week  | Phase              | Deliverables                                      |
| ----- | ------------------ | ------------------------------------------------- |
| 1-4   | Project Definition | This document (Milestone 1)                       |
| 5-6   | Data Preparation   | EDA, preprocessing, feature engineering           |
| 6-7   | Baseline Model     | Logistic regression implementation and evaluation |
| 7-8   | Improved Model     | XGBoost/Random Forest with tuning (Milestone 2)   |
| 9-10  | Interpretation     | SHAP analysis, feature importance                 |
| 11-12 | Final Report       | Documentation, code cleanup (Milestone 3)         |

---

## 8. Conclusion

This project presents a well-scoped, feasible approach to customer churn prediction using machine learning. By leveraging a clean, well-documented dataset and established ML techniques, the project will deliver:

1. A complete end-to-end prediction pipeline
2. Rigorous model evaluation and comparison
3. Interpretable results with actionable business insights

The bounded scope ensures completion within the 12-week timeline while maintaining sufficient technical depth for a capstone project.

---

**Word Count:** ~1,200 words | **Page Count:** 3 pages (formatted)

---

*Document Version 1.0 | February 2026*
