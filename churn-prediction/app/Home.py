"""Home page — project overview and navigation guide."""

import streamlit as st

st.set_page_config(
    page_title="Telco Churn Predictor",
    page_icon="📡",
    layout="wide",
)

st.title("📡 Telco Customer Churn Predictor")
st.caption("CS5998 Capstone Project · MDSAI")

st.markdown(
    """
    This app accompanies the **Customer Churn Prediction** capstone project.
    It exposes three tools built on top of Logistic Regression and XGBoost
    classifiers trained on the IBM Telco Customer Churn dataset.

    ---

    ### Pages

    | Page | Description |
    |------|-------------|
    | **Predict** | Enter a single customer's details and get a churn probability with a SHAP explanation |
    | **Dashboard** | Compare model performance — confusion matrices, ROC curves, and metric cards |
    | **Bulk Score** | Upload a CSV of customers and download a scored result file |

    ---

    ### Dataset
    IBM Telco Customer Churn · 7 043 customers · 19 features  
    Target: `Churn` (binary — Yes / No)

    ### Models
    - Logistic Regression (`class_weight='balanced'`)
    - XGBoost (`scale_pos_weight` tuned to class imbalance)

    Both models were trained on an 80/20 stratified split (`random_state=42`).
    Preprocessing: `StandardScaler` on numerics, `OneHotEncoder` on categoricals.
    """
)

st.info("Use the sidebar on the left to navigate between pages.", icon="👈")
