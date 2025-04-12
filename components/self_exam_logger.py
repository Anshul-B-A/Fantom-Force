import streamlit as st
import pandas as pd
from datetime import datetime
from utils.supabase_client import supabase
import os

SYMPTOM_CSV_COLUMNS = [
    "date", "dimpling", "swelling", "inverted_nipple",
    "redness", "nipple_discharge", "lump", "pain"
]

LOG_FILE = "data/symptom_logs.csv"

def log_to_supabase(data):
    try:
        supabase.table("symptom_logs").insert(data).execute()
        return True
    except Exception as e:
        st.warning(f"Supabase logging failed: {e}")
        return False

def log_to_csv(symptom_data):
    # Ensure the columns include the necessary ones
    extended_columns = SYMPTOM_CSV_COLUMNS + ["notes", "risk_level"]  # Add risk_level and notes to the CSV

    # Check if the CSV exists
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        # Remove any potential duplicates based on today's date
        df = df[df["date"] != datetime.now().strftime("%Y-%m-%d")]
    else:
        df = pd.DataFrame(columns=extended_columns)

    # Prepare the data to be logged
    today = datetime.now().strftime("%Y-%m-%d")
    notes = symptom_data.get("notes", "").strip()
    notes = notes if notes else "none"
    
    csv_data = {
        "date": today,
        "dimpling": symptom_data["dimpling"],
        "swelling": symptom_data["swelling"],
        "inverted_nipple": symptom_data["inverted_nipple"],
        "redness": symptom_data["redness"],
        "nipple_discharge": symptom_data["nipple_discharge"],
        "lump": symptom_data["lump"],
        "pain": symptom_data["pain"],
        "notes": notes,
        "risk_level": symptom_data.get("risk_level", "none")  # Store risk level
    }

    # Append the new data to the DataFrame and write back to CSV (with header only if file is new)
    df = pd.concat([df, pd.DataFrame([csv_data])], ignore_index=True)
    df.to_csv(LOG_FILE, mode='w', header=True, index=False)  # Always write with header to ensure it's correct

    st.success("✅ Saved symptoms locally in CSV")

import streamlit as st
import pandas as pd
from datetime import datetime
import os

SYMPTOM_CSV_COLUMNS = [
    "date", "dimpling", "swelling", "inverted_nipple",
    "redness", "nipple_discharge", "lump", "pain", "notes", "risk_level"
]

LOG_FILE = "data/symptom_logs.csv"

def log_to_csv(symptom_data):
    if os.path.exists(LOG_FILE):
        try:
            df = pd.read_csv(LOG_FILE)
            if df.empty:
                raise ValueError("CSV is empty")
        except (pd.errors.EmptyDataError, ValueError):
            df = pd.DataFrame(columns=SYMPTOM_CSV_COLUMNS)
    else:
        df = pd.DataFrame(columns=SYMPTOM_CSV_COLUMNS)

    today = datetime.now().strftime("%Y-%m-%d")
    df = df[df["date"] != today]  # Avoid duplicate entries for today

    df = pd.concat([df, pd.DataFrame([symptom_data])], ignore_index=True)
    df.to_csv(LOG_FILE, index=False)
    st.success("✅ Saved symptoms locally in CSV")


def self_exam_logger(email=None, user_id=None):
    st.markdown("## 🩺 Self Breast Exam Form")
    with st.container():
        with st.form("self_exam_form"):
            st.markdown("### 👀 Visual Symptoms")
            vis_dimpling = st.checkbox("Dimpling or puckering of skin")
            vis_swelling = st.checkbox("Swelling or distortion")
            vis_nipple_change = st.checkbox("Inverted or shifted nipple")
            vis_rash = st.checkbox("Redness, rash, or soreness")
            vis_discharge = st.selectbox("Nipple discharge", ["None", "Watery", "Milky", "Yellow", "Bloody"])

            st.markdown("### 🖐️ Touch Symptoms")
            lump_present = st.checkbox("Felt any lump or mass")
            st.selectbox("Lump side", ["None", "Left", "Right", "Both"]) if lump_present else "None"
            tenderness = st.checkbox("Tenderness or pain")

            st.markdown("### 📝 Additional Info")
            notes = st.text_area("Notes (optional)", placeholder="Mention any observations, pain duration, etc.")
            exam_date = st.date_input("Date of self-exam", value=datetime.now().date())
            st.selectbox("Language used", ["English", "Kannada", "Hindi", "Malayalam"])

            submitted = st.form_submit_button("✅ Submit Exam Report")

        if submitted:
            score = sum([
                vis_dimpling, vis_swelling, vis_nipple_change,
                vis_rash, vis_discharge != "None", lump_present, tenderness
            ])
            risk_level = (
                "Low" if score <= 1 else
                "Moderate" if score <= 3 else
                "High"
            )
            st.markdown(f"### 📊 Risk Level: **{risk_level} Risk**")

            selected_symptoms = []
            if vis_dimpling: selected_symptoms.append("Skin Dimpling")
            if vis_swelling: selected_symptoms.append("Swelling")
            if vis_nipple_change: selected_symptoms.append("Nipple Change")
            if vis_rash: selected_symptoms.append("Rash/Redness")
            if vis_discharge != "None": selected_symptoms.append(f"Discharge: {vis_discharge}")
            if lump_present: selected_symptoms.append("Lump")
            if tenderness: selected_symptoms.append("Tenderness")

            # Prepare data for CSV logging
            csv_data = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "dimpling": vis_dimpling,
                "swelling": vis_swelling,
                "inverted_nipple": vis_nipple_change,
                "redness": vis_rash,
                "nipple_discharge": vis_discharge != "None",
                "lump": lump_present,
                "pain": tenderness,
                "notes": notes.strip() if notes.strip() else "none",
                "risk_level": risk_level
            }
            log_to_csv(csv_data)

            return csv_data  # optional return for later use
