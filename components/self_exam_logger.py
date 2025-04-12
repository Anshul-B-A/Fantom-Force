import streamlit as st
import pandas as pd
from datetime import datetime
from utils.supabase_client import supabase
import os

def log_to_supabase(data):
    try:
        supabase.table("symptom_logs").insert(data).execute()
        return True
    except Exception as e:
        st.warning(f"Supabase logging failed: {e}")
        return False

def log_to_csv(data, csv_path):
    import json
    data["selected_symptoms"] = json.dumps(data["selected_symptoms"])
    df = pd.DataFrame([data])

    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_path, mode='w', header=True, index=False)
    st.success("Saved locally in CSV as fallback 📁")

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
            lump_side = st.selectbox("Lump side", ["None", "Left", "Right", "Both"]) if lump_present else "None"
            tenderness = st.checkbox("Tenderness or pain")

            st.markdown("### 📝 Additional Info")
            notes = st.text_area("Notes (optional)", placeholder="Mention any observations, pain duration, etc.")
            exam_date = st.date_input("Date of self-exam", value=datetime.now().date())
            language = st.selectbox("Language used", ["English", "Kannada", "Hindi", "Malayalam"])

            submitted = st.form_submit_button("✅ Submit Exam Report")

        if submitted:
            # Risk Scoring
            score = sum([
                vis_dimpling, vis_swelling, vis_nipple_change,
                vis_rash, vis_discharge != "None",
                lump_present, tenderness
            ])
            risk_level = (
                "🟢 Low" if score <= 1 else
                "🟡 Moderate" if score <= 3 else
                "🔴 High"
            )

            st.markdown(f"### 📊 Risk Level: **{risk_level} Risk**")

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
                "risk_level": risk_level.split()[1],  # Low/Moderate/High
                "notes": notes,
                "lump_side": lump_side,
                "discharge_type": vis_discharge
            }

            if log_to_supabase(log_data):
                st.success("Self-exam saved to Supabase ✅")
            else:
                log_to_csv(log_data, "data/symptom_logs.csv")
