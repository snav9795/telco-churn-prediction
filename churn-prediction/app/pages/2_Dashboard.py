"""Model performance dashboard — confusion matrices, ROC curves, metric cards."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)

from utils import load_artifacts, load_test_data

st.set_page_config(page_title="Dashboard · Churn", page_icon="📊", layout="wide")
st.title("📊 Model Performance Dashboard")

preprocessor, lr, xgb = load_artifacts()
test_df = load_test_data()

X_test = test_df.drop(columns=["Churn"]).values
y_test = test_df["Churn"].values


def compute_metrics(name, model):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    return {
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1": f1_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_prob),
    }, y_pred, y_prob


lr_metrics, lr_pred, lr_prob = compute_metrics("Logistic Regression", lr)
xgb_metrics, xgb_pred, xgb_prob = compute_metrics("XGBoost", xgb)

metrics_df = pd.DataFrame([lr_metrics, xgb_metrics]).set_index("Model")

# ── Metric cards ──────────────────────────────────────────────────────────────
st.subheader("Key metrics — test set")
model_tab = st.radio("Select model", ["Logistic Regression", "XGBoost"], horizontal=True)

selected = lr_metrics if model_tab == "Logistic Regression" else xgb_metrics
cols = st.columns(5)
for col, key in zip(cols, ["Accuracy", "Precision", "Recall", "F1", "ROC-AUC"]):
    col.metric(key, f"{selected[key]:.4f}")

# ── Comparison table ──────────────────────────────────────────────────────────
st.subheader("Model comparison")
st.dataframe(metrics_df.style.format("{:.4f}").highlight_max(axis=0, color="#d4edda"), use_container_width=True)

# ── Confusion matrices ────────────────────────────────────────────────────────
st.subheader("Confusion matrices")
fig_cm, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, model, name, y_pred in zip(
    axes,
    [lr, xgb],
    ["Logistic Regression", "XGBoost"],
    [lr_pred, xgb_pred],
):
    ConfusionMatrixDisplay.from_predictions(
        y_test, y_pred,
        display_labels=["No Churn", "Churn"],
        cmap="Blues",
        ax=ax,
    )
    ax.set_title(name)
plt.tight_layout()
st.pyplot(fig_cm, bbox_inches="tight")

# ── ROC curves ────────────────────────────────────────────────────────────────
st.subheader("ROC curves")
fig_roc = go.Figure()
for name, prob, auc in [
    ("Logistic Regression", lr_prob, lr_metrics["ROC-AUC"]),
    ("XGBoost", xgb_prob, xgb_metrics["ROC-AUC"]),
]:
    fpr, tpr, _ = roc_curve(y_test, prob)
    fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, name=f"{name} (AUC={auc:.4f})"))

fig_roc.add_shape(type="line", x0=0, y0=0, x1=1, y1=1,
                  line=dict(dash="dash", color="grey"))
fig_roc.update_layout(
    xaxis_title="False Positive Rate",
    yaxis_title="True Positive Rate",
    legend=dict(x=0.6, y=0.1),
    height=450,
)
st.plotly_chart(fig_roc, use_container_width=True)
