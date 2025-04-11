# ✅ MUST be the first Streamlit command
import streamlit as st
st.set_page_config(page_title="Dashboard", page_icon="🧭", layout="wide")
####### language --------------------------
# Set default language if not already set
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# Language selector
language_options = {
    "English": "en",
    "हिंदी": "hi",
    "ಕನ್ನಡ": "kn",
    "മലയാളം": "ml"
}
selected_lang = st.selectbox("🌐 Select Language", list(language_options.keys()))
st.session_state.lang = language_options[selected_lang]
######-----------------------------------

import time
import requests
from utils.translation import t  # 👈 Import translation helper
from utils.groq_helper import stream_groq_chat

# ✅ Optional: Redirect if not logged in
# if "user" not in st.session_state:
#     st.warning(translate("Please log in first."))
#     st.switch_page("app.py")

# Header
st.title(t("🧭 Dashboard - Breast Cancer Support App"))

# Tabs for each feature
tab1, tab2, tab3, tab4 = st.tabs([
    t("🤖 GenAI Chatbot"), 
    t("🩺 Symptom Checker"), 
    t("📍 Find Nearby Hospitals"), 
    t("🗣️ Community & Resources")
])

# ---------------------------------------
# 🤖 GenAI Chatbot
# ---------------------------------------
with tab1:
    st.subheader(t("🤖 GenAI Chatbot (Groq-powered)"))

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history (top to bottom)
    st.markdown("### " + t("🗨️ Chat"))
    chat_container = st.container()
    with chat_container:
        for role, msg in st.session_state.chat_history:
            if role == "user":
                st.markdown(f"**🧑 {t('You')}:** {msg}")
            elif role == "bot":
                st.markdown(f"**🤖 {t('nariSaathi')}:** {msg}")
        scroll_spacer = st.empty()  # Helps with auto-scroll

    # Input box stays at the bottom
    st.divider()
    user_input = st.text_input(
        t("Ask something about breast cancer"),
        key="chat_input",
        placeholder=t("Type here and press send...")
    )

    if st.button(t("Send"), key="send_btn") and user_input.strip():
        st.session_state.chat_history.append(("user", user_input.strip()))

        full_response = ""
        placeholder = scroll_spacer.empty()
        try:
            for chunk in stream_groq_chat(user_input, st.secrets["GROK_API_KEY"]):
                full_response += chunk
                placeholder.markdown(f"**🤖 {t('nariSaathi')}:** {full_response}▌")
                time.sleep(0.03)
            placeholder.markdown(f"**🤖 {t('nariSaathi')}:** {full_response}")
            st.session_state.chat_history.append(("bot", full_response))
        except Exception as e:
            st.error(f"{t('Error')}: {str(e)}")

# ---------------------------------------
# 🩺 Symptom Checker (Stub)
# ---------------------------------------

import pandas as pd
from datetime import datetime
from supabase import create_client, Client  # For Supabase integration

# Initialize Supabase client (if using Supabase)
SUPABASE_URL = st.secrets.get("SUPABASE_URL", None)
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", None)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

# Function to save data locally or to Supabase
def save_symptom_data(data):
    if supabase:
        try:
            response = supabase.table("symptom_logs").insert(data).execute()
            if response.status_code == 201:
                st.success(t("Data saved successfully to Supabase!"))
            else:
                st.error(t("Failed to save data to Supabase."))
        except Exception as e:
            st.error(f"{t('Error saving to Supabase')}: {str(e)}")
    else:
        # Save to local CSV
        try:
            import json
            data["selected_symptoms"] = json.dumps(data["selected_symptoms"])
            import json
            data["selected_symptoms"] = json.dumps(data["selected_symptoms"])
            df = pd.DataFrame([data])


            csv_file = "data/symptom_logs.csv"
            if not os.path.exists(csv_file):
                df.to_csv(csv_file, index=False)
            else:
                df.to_csv(csv_file, mode="a", header=False, index=False)
            st.success(t("Data saved successfully to local CSV!"))
        except Exception as e:
            st.error(f"{t('Error saving to CSV')}: {str(e)}")

with tab2:
    from components.self_exam_logger import self_exam_logger

    # Pass user's email or user_id if authenticated
    self_exam_logger(email=st.session_state.get("email"), user_id=st.session_state.get("user_id"))

    from components.self_exam_plots import render_self_exam_dashboard
    render_self_exam_dashboard()

# ---------------------------------------
# 📍 Hospital Locator (Stub)
# ---------------------------------------
with tab3:
    st.subheader(t("📍 Find Nearby Hospitals"))

    st.markdown(t("""
    Use the button below to explore nearby cancer clinics.
    """))

    api_key = st.secrets["GCP_MAPS_API_KEY"]  # add your API key in .streamlit/secrets.toml

    html_code = f"""
    <div id="map" style="height: 600px; width: 100%; margin-top: 10px;"></div>

    <script>
    function initMap() {{
        navigator.geolocation.getCurrentPosition(function(position) {{
            var userLocation = {{
                lat: position.coords.latitude,
                lng: position.coords.longitude
            }};

            var map = new google.maps.Map(document.getElementById('map'), {{
                center: userLocation,
                zoom: 14
            }});

            var marker = new google.maps.Marker({{
                position: userLocation,
                map: map,
                title: "You are here",
                icon: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
            }});
        }});
    }}
    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap" async defer></script>
    """

    st.components.v1.html(html_code, height=650)

    # Redirect button to Google Maps
    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 20px;'>
            <a href="https://www.google.com/maps/search/breast+cancer+clinics+near+me/" target="_blank">
                <button style="
                padding: 10px 20px;
                font-size: 16px;
                background-color: #1e1e1e;
                color: white;
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 8px;
                cursor: pointer;
                transition: all 0.3s ease;">
                    {t("🔍 Open Google Maps to Locate Nearby Clinics")}
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
# ---------------------------------------
# 🗣️ Community & Resources (Stub)
# ---------------------------------------
with tab4:
    st.subheader(t("🗣️ Community Forum & Resources"))
    st.info(t("Curated info, posts, and text-to-speech support will go here."))

