import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
from datetime import datetime
from utils.translation import t

CSV_PATH = "data/symptom_logs.csv"

def load_logs():
    if not os.path.exists(CSV_PATH):
        st.warning("No logs found yet.")
        return pd.DataFrame()

    df = pd.read_csv(CSV_PATH, on_bad_lines="skip")  # Skip malformed lines

    # Parse symptoms column safely
    def safe_json_loads(value):
        if isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return []
        return []

    if "selected_symptoms" in df.columns:
        df["selected_symptoms"] = df["selected_symptoms"].apply(safe_json_loads)

    # Parse timestamp with specified format (you can adjust this format based on your actual timestamp format)
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
    else:
        df["timestamp"] = pd.Timestamp.now()

    # Ensure risk_factor exists
    if "risk_factor" not in df.columns:
        df["risk_factor"] = "Unknown"

    return df

def plot_riskfactor_over_time(df):
    st.markdown("### ⏳ Risk Factor Over Time")

    df_sorted = df.sort_values("timestamp")

    # Map risk levels and color
    risk_map = {"Low": 1, "Moderate": 2, "High": 3}
    color_map = {1: "green", 2: "gold", 3: "red"}

    df_sorted["risk_numeric"] = df_sorted["risk_factor"].map(risk_map)

    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot the line
    ax.plot(df_sorted["timestamp"], df_sorted["risk_numeric"], marker='o', linewidth=2, color='black', zorder=1)

    # Scatter points with colors
    for _, row in df_sorted.iterrows():
        ax.scatter(row["timestamp"], row["risk_numeric"], color=color_map[row["risk_numeric"]], s=100, zorder=2)

    # Axis setup
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Risk Level (1 = Low, 2 = Moderate, 3 = High)")
    ax.set_title("Risk Factor Trend Over Time")
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["Low", "Moderate", "High"])

    plt.xticks(rotation=45, ha="right")
    ax.grid(True, linestyle="--", alpha=0.6)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='green', label='Low'),
        Patch(facecolor='gold', label='Moderate'),
        Patch(facecolor='red', label='High')
    ]
    ax.legend(handles=legend_elements)

    st.pyplot(fig)

def render_self_exam_dashboard():
    df = load_logs()
    if df.empty:
        return

    st.markdown("## 📊 Self Exam Dashboard")
    with st.expander("📁 View Raw Data"):
        st.dataframe(df)

    plot_riskfactor_over_time(df)


