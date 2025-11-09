%%writefile app.py
import pandas as pd
import numpy as np
from pathlib import Path
import streamlit as st
import joblib
import plotly.express as px

ART = Path("/kaggle/working/artifacts")

st.set_page_config(page_title="AI Multi-Agent Stock Analyzer", layout="wide")
st.title("🧠 AI Multi-Agent Stock Analyzer — Short Candidates")

# --- Load artifacts ---
def safe_read_csv(p, **kw):
    p = ART / p
    return pd.read_csv(p, **kw) if p.exists() else pd.DataFrame()

metrics = {}
mfile = ART / "metrics.csv"
if mfile.exists():
    mser = pd.read_csv(mfile, header=None, index_col=0).squeeze("columns")
    metrics = {k: float(v) for k, v in mser.to_dict().items()}

today_scores = safe_read_csv("today_scores.csv")
picks        = safe_read_csv("picks.csv")
equity       = safe_read_csv("equity_curve.csv")
narr         = (ART/"narrative.txt").read_text() if (ART/"narrative.txt").exists() else "No narrative."

# --- Metrics header ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("AUROC", f"{metrics.get('auroc', np.nan):.3f}")
col2.metric("PR-AUC", f"{metrics.get('pr_auc', np.nan):.3f}")
col3.metric("Best threshold", f"{metrics.get('best_thr', np.nan):.2f}")
col4.metric("Precision@10", f"{metrics.get('precision@10', np.nan):.2f}")

# --- Narrative ---
with st.expander("Agent narrative (rule-based rationale)"):
    st.text(narr)

# --- Today scores table ---
st.subheader("Today’s scores (after liquidity/price filters)")
if not today_scores.empty:
    st.dataframe(today_scores.head(200))
else:
    st.info("No scores available.")

# --- Picks table ---
st.subheader("Top-K short picks")
if not picks.empty:
    st.dataframe(picks)
else:
    st.info("No picks available.")

# --- Backtest chart ---
st.subheader("Toy backtest equity (Top-K short, N-day hold)")
if not equity.empty and {"step","equity"}.issubset(equity.columns):
    fig = px.line(equity, x="step", y="equity", title="Equity Curve")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No equity curve logged.")

# --- Live inference demo (optional, file upload) ---
st.subheader("Try a custom CSV (optional)")
u = st.file_uploader("Upload a CSV with feature columns", type=["csv"])
if u is not None:
    df = pd.read_csv(u)
    need = ["ret1","rvol20","ma_ratio","rsi14","volume_adj"]
    if not set(need).issubset(df.columns):
        st.warning(f"CSV must contain: {need}")
    else:
        # Load model
        model_path = ART/"model_pipeline.pkl"
        if model_path.exists():
            model = joblib.load(model_path)
            df["prob"] = model.predict_proba(df[need])[:,1]
            st.success("Scored uploaded file.")
            st.dataframe(df.sort_values("prob", ascending=False).head(50))
        else:
            st.error("Model file not found: model_pipeline.pkl")
