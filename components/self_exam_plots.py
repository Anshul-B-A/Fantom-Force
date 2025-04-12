import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
from datetime import datetime
from utils.translation import t
CSV_PATH = "data/symptom_logs.csv"

SYMPTOM_CSV_COLUMNS = [
    "date", "dimpling", "swelling", "inverted_nipple",
    "redness", "nipple_discharge", "lump", "pain"
]

def load_logs():
    if not os.path.exists(CSV_PATH):
        st.warning("No logs found yet.")
        return pd.DataFrame(columns=SYMPTOM_CSV_COLUMNS)  # Return an empty DataFrame with the correct columns

    try:
        df = pd.read_csv(CSV_PATH)
        if df.empty:
            raise pd.errors.EmptyDataError("CSV is empty")  # Explicitly raise error if data is empty
    except pd.errors.EmptyDataError:
        # If the file is empty, return an empty DataFrame with the expected columns
        st.warning("CSV file is empty.")
        return pd.DataFrame(columns=SYMPTOM_CSV_COLUMNS)  # Adjust to your column names

    # Ensure 'created_at' column exists
    if "created_at" not in df.columns:
        df["created_at"] = pd.Timestamp.now()

    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    # Ensure 'score' column exists
    if "score" not in df.columns:
        df["score"] = 0  # Default value for missing scores

    # Ensure 'risk_level' column exists
    if "risk_level" not in df.columns:
        df["risk_level"] = "Unknown"  # Default value for missing risk levels

    return df



def plot_risk_over_time(df):
    st.markdown("### 📅 Risk Score Over Time")
    df_sorted = df.sort_values("created_at")
    fig, ax = plt.subplots()
    ax.plot(df_sorted["created_at"], df_sorted["score"], marker='o', linestyle='-')
    ax.set_xlabel("Date")
    ax.set_ylabel("Risk Score")
    ax.set_title("Risk Score Trend")
    st.pyplot(fig)

def plot_risk_levels(df):
    st.markdown("### 🟢🟡🔴 Risk Level Distribution")
    risk_counts = df["risk_level"].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=risk_counts.index, y=risk_counts.values, ax=ax, palette="Set2")
    ax.set_ylabel("Count")
    ax.set_title("Risk Level Counts")
    st.pyplot(fig)

def plot_common_symptoms(df):
    st.markdown("### 🔍 Most Frequent Symptoms Reported")
    
    # Count how many times each symptom was reported as True
    symptom_counts = df.drop(columns=["date", "created_at", "score", "risk_level"], errors="ignore").sum().sort_values(ascending=False)

    symptom_df = pd.DataFrame({
        "Symptom": symptom_counts.index,
        "Count": symptom_counts.values
    })

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=symptom_df, x="Count", y="Symptom", ax=ax, palette="Blues_r")
    ax.set_title("Top Reported Symptoms")
    st.pyplot(fig)


def render_self_exam_dashboard():
    df = load_logs()
    if df.empty:
        return
    st.markdown("## 📈 Self Exam Analytics Dashboard")
    with st.expander("📁 Raw Log Table", expanded=False):
        st.dataframe(df)

    plot_risk_over_time(df)
    plot_risk_levels(df)
    plot_common_symptoms(df)
