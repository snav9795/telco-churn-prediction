"""Bulk scoring — upload a CSV, score it, download results."""

import io

import pandas as pd
import streamlit as st

from utils import CATEGORICAL_COLS, NUMERIC_COLS, load_artifacts

st.set_page_config(page_title="Bulk Score · Churn", page_icon="📂", layout="wide")
st.title("📂 Bulk Customer Scoring")

with st.spinner("Loading model artifacts…"):
    preprocessor, lr, xgb = load_artifacts()

st.markdown(
    """
    Upload a CSV file containing raw customer features (same columns as the
    IBM Telco dataset, **excluding** `customerID` and `Churn`).
    The app will append `churn_prob_lr`, `churn_prob_xgb`, and `predicted_churn`
    columns (XGBoost prediction at 0.5 threshold) and let you download the result.
    """
)

REQUIRED_COLS = NUMERIC_COLS + CATEGORICAL_COLS

with st.expander("Expected columns"):
    st.write(REQUIRED_COLS)

uploaded = st.file_uploader("Upload customer CSV", type=["csv"])
model_choice = st.radio("Scoring model for predicted_churn column",
                        ["XGBoost", "Logistic Regression"], horizontal=True)

if uploaded is not None:
    raw = pd.read_csv(uploaded)
    raw.columns = raw.columns.str.strip()

    if "customerID" in raw.columns:
        raw = raw.drop(columns=["customerID"])
    if "Churn" in raw.columns:
        raw = raw.drop(columns=["Churn"])

    missing = [c for c in REQUIRED_COLS if c not in raw.columns]
    if missing:
        st.error(f"Missing required columns: {missing}")
    else:
        with st.spinner("Scoring…"):
            X = preprocessor.transform(raw[REQUIRED_COLS])
            lr_prob = lr.predict_proba(X)[:, 1]
            xgb_prob = xgb.predict_proba(X)[:, 1]
            chosen_prob = xgb_prob if model_choice == "XGBoost" else lr_prob

        result = raw.copy()
        result["churn_prob_lr"] = lr_prob.round(4)
        result["churn_prob_xgb"] = xgb_prob.round(4)
        result["predicted_churn"] = (chosen_prob >= 0.5).astype(int)

        st.success(f"Scored {len(result):,} rows.")
        st.dataframe(result.head(20), use_container_width=True)

        high_risk = (result["predicted_churn"] == 1).sum()
        st.metric("High-risk customers (≥ 50% churn probability)", high_risk,
                  delta=f"{high_risk / len(result):.1%} of upload")

        csv_bytes = result.to_csv(index=False).encode()
        st.download_button(
            "Download scored CSV",
            data=csv_bytes,
            file_name="churn_scores.csv",
            mime="text/csv",
        )

st.divider()
st.caption("CS5998 Capstone · Master of Data Science & AI")
