# Concepts reference — quick glossary

One-line definitions for terms used across the 7-day churn project.

---

## Machine learning core

| Term | Meaning |
|------|---------|
| **Machine learning** | Learning a mapping from inputs to outputs from data, instead of hand-writing all rules. |
| **Supervised learning** | Training with labeled examples (here: customer features + churn Yes/No). |
| **Binary classification** | Predicting one of two classes (churn / no churn). |
| **Feature** | One input column (e.g. `tenure`, `Contract`). |
| **Label / target** | What you predict (`Churn`). |
| **EDA** | Exploratory data analysis: plots and tables to understand data before modeling. |
| **Distribution** | How values spread (histograms, counts for categories). |
| **Correlation** | Linear association strength between numeric variables (−1 to 1). |
| **Class imbalance** | When one outcome is much rarer (here ~26% churn vs ~74% no churn). |
| **Train/test split** | Hold out data the model never trains on, to estimate real-world performance. |
| **Stratified split** | Split that keeps churn proportion similar in train and test. |
| **Cross-validation** | Repeated train/validate folds to tune models without peeking at the test set. |
| **Data leakage** | Using information that would not be available at prediction time (inflates scores). |
| **Overfitting** | Model memorizes training noise; poor test performance. |
| **Regularization** | Penalty that discourages overly complex models (e.g. in logistic regression). |
| **Hyperparameter** | Setting chosen before training (e.g. tree depth, learning rate). |

## Data preparation

| Term | Meaning |
|------|---------|
| **One-hot encoding** | Turn categories into 0/1 columns per level (e.g. `Contract_Month-to-month`). |
| **Label encoding** | Assign integers to categories; can imply false ordering—use carefully. |
| **Imputation** | Filling missing values (e.g. median, or zero for “new” total charges). |
| **Scaling / normalization** | Put numeric features on comparable scales (often for linear models). |
| **SMOTE** | Synthetic oversampling of minority class (optional; not always needed). |

## Models

| Term | Meaning |
|------|---------|
| **Logistic regression** | Linear model + sigmoid → probability of class 1; strong baseline for tabular data. |
| **Sigmoid** | S-shaped function mapping scores to probabilities between 0 and 1. |
| **Decision tree** | Sequence of if/else rules on features. |
| **Ensemble** | Combine many models (e.g. random forest, gradient boosting). |
| **Boosting** | Sequentially add trees that correct previous errors (XGBoost is a popular implementation). |
| **XGBoost** | Gradient boosted trees; often strong on structured data. |

## Evaluation

| Term | Meaning |
|------|---------|
| **Confusion matrix** | Counts of TP, TN, FP, FN. |
| **Accuracy** | Fraction of correct predictions; misleading when classes are imbalanced. |
| **Precision** | Of predicted churns, how many truly churned. |
| **Recall** | Of actual churners, how many you caught. |
| **F1-score** | Harmonic mean of precision and recall. |
| **ROC-AUC** | Ability to rank positives above negatives across thresholds; threshold-free summary. |
| **Threshold** | Probability cutoff above which you predict “churn” (default often 0.5). |

## Interpretation

| Term | Meaning |
|------|---------|
| **Feature importance** | Model-specific ranking of how much each feature drives predictions. |
| **SHAP** | Shapley-based attribution of each feature’s push toward churn vs not churn for a prediction. |
| **Waterfall plot** | SHAP view showing how each feature moves prediction from base to final. |
| **Summary plot** | SHAP overview of feature effects across many rows. |

## Product & delivery

| Term | Meaning |
|------|---------|
| **Streamlit** | Python library to build interactive web UIs for ML/data apps quickly. |
| **Deployment** | Running the app on a server others can reach (e.g. Streamlit Community Cloud). |
| **Git** | Version control: track changes locally. |
| **GitHub** | Host Git repositories online for sharing and collaboration. |
| **Reproducibility** | Someone else can reinstall deps and rerun your pipeline with the same results. |
| **`requirements.txt`** | Pinned or listed Python packages for `pip install -r`. |

---

For day-by-day tasks, use `01_Day1_Guide.md` … `07_Day7_Guide.md`.
