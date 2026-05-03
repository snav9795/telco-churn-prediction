"""Single-customer churn prediction with optional SHAP waterfall."""

import numpy as np
import pandas as pd
import shap
import streamlit as st

from utils import (
    CATEGORICAL_COLS,
    CATEGORICAL_OPTIONS,
    NUMERIC_COLS,
    load_artifacts,
)

st.set_page_config(page_title="Predict · Churn", page_icon="🔮", layout="wide")
st.title("🔮 Single-Customer Prediction")

with st.spinner("Loading model artifacts…"):
    preprocessor, lr, xgb = load_artifacts()


def build_input_row():
    st.subheader("Customer details")
    col1, col2, col3 = st.columns(3)

    with col1:
        senior = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x else "No")
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        monthly = st.number_input("Monthly Charges ($)", 0.0, 200.0, 65.0, step=0.5)
        total = st.number_input("Total Charges ($)", 0.0, 10000.0, float(tenure * monthly), step=1.0)

    with col2:
        cat_vals = {}
        for col in CATEGORICAL_COLS[:8]:
            cat_vals[col] = st.selectbox(col, CATEGORICAL_OPTIONS[col])

    with col3:
        for col in CATEGORICAL_COLS[8:]:
            cat_vals[col] = st.selectbox(col, CATEGORICAL_OPTIONS[col])

    row = {"SeniorCitizen": senior, "tenure": tenure,
           "MonthlyCharges": monthly, "TotalCharges": total}
    row.update(cat_vals)
    return pd.DataFrame([row])


raw_df = build_input_row()
model_choice = st.radio("Model", ["Logistic Regression", "XGBoost"], horizontal=True)
show_shap = st.checkbox("Show SHAP waterfall", value=True)

if st.button("Predict", type="primary"):
    with st.spinner("Running model…"):
        X = preprocessor.transform(raw_df)
        model = lr if model_choice == "Logistic Regression" else xgb
        prob = model.predict_proba(X)[0, 1]

    risk_label = "🔴 High risk" if prob >= 0.5 else "🟢 Low risk"
    st.metric("Churn probability", f"{prob:.1%}", delta=risk_label, delta_color="off")

    col_a, col_b = st.columns(2)
    col_a.progress(float(prob))
    col_b.write(f"Predicted class: **{'Churn' if prob >= 0.5 else 'No Churn'}**")

    if show_shap and model_choice == "XGBoost":
        with st.spinner("Computing SHAP values…"):
            explainer = shap.TreeExplainer(xgb)
            shap_vals = explainer(X)
        feature_names = preprocessor.get_feature_names_out()
        # strip transformer prefixes added by ColumnTransformer
        feature_names = [n.split("__")[-1] for n in feature_names]
        shap_vals.feature_names = list(feature_names)
        fig, ax = __import__("matplotlib.pyplot", fromlist=["pyplot"]).subplots()
        shap.plots.waterfall(shap_vals[0], max_display=15, show=False)
        st.pyplot(fig, bbox_inches="tight")
    elif show_shap and model_choice == "Logistic Regression":
        st.info("SHAP waterfall is available for XGBoost only in this app.")

st.divider()
st.caption("CS5998 Capstone · Master of Data Science & AI")
