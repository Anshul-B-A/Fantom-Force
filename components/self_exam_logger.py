import streamlit as st
import pandas as pd
import os
from datetime import datetime
import json

def log_to_csv(data, csv_path):
    data["selected_symptoms"] = json.dumps(data["selected_symptoms"])

    # Ensure consistent column order
    ordered_cols = [
        "created_at", "email", "user_id", "exam_date", "language",
        "selected_symptoms", "score", "risk_level", "notes",
        "lump_side", "discharge_type"
    ]
    df = pd.DataFrame([data])[ordered_cols]

    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_path, mode='w', header=True, index=False)
    st.success("Saved data! 📁")

def self_exam_logger(email=None, user_id=None):
    st.markdown("## 🩺 Self Breast Examination Log:")
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
            lump_side = st.selectbox("Lump side", ["None", "Left", "Right", "Both"]) if lump_present else "None"
            tenderness = st.checkbox("Tenderness or pain")

            st.markdown("### 📝 Additional Info")
            notes = st.text_area("Notes (optional)", placeholder="Mention any observations, pain duration, etc.")
            exam_date = st.date_input("Date of self-exam", value=datetime.now().date())
            language = st.selectbox("Language used", ["English", "Kannada", "Hindi", "Malayalam"])

            submitted = st.form_submit_button("✅ Submit Exam Report")

        if submitted:
            # Rule-based Risk Scoring (+1 per symptom)
            score = sum([
                vis_dimpling, vis_swelling, vis_nipple_change,
                vis_rash, vis_discharge != "None",
                lump_present, tenderness
            ])
            risk_text = (
                "Low" if score <= 1 else
                "Moderate" if score <= 3 else
                "High"
            )
            risk_emoji = {
                "Low": "🟢",
                "Moderate": "🟡",
                "High": "🔴"
            }[risk_text]

            st.markdown(f"### 📊 Risk Level: **{risk_emoji} {risk_text} Risk**")

            selected_symptoms = []
            if vis_dimpling: selected_symptoms.append("Skin Dimpling")
            if vis_swelling: selected_symptoms.append("Swelling")
            if vis_nipple_change: selected_symptoms.append("Nipple Change")
            if vis_rash: selected_symptoms.append("Rash/Redness")
            if vis_discharge != "None": selected_symptoms.append(f"Discharge: {vis_discharge}")
            if lump_present: selected_symptoms.append(f"Lump: {lump_side}")
            if tenderness: selected_symptoms.append("Tenderness")

            log_data = {
                "created_at": datetime.now().isoformat(),
                "email": email or "guest@mammo.app",
                "user_id": user_id,
                "exam_date": str(exam_date),
                "language": language,
                "selected_symptoms": selected_symptoms,
                "score": score,
                "risk_level": risk_text,  # Only "Low", "Moderate", "High"
                "notes": notes,
                "lump_side": lump_side,
                "discharge_type": vis_discharge
            }

            log_to_csv(log_data, "data/symptom_logs.csv")
