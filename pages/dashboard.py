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
with tab2:
    st.subheader(t("🩺 Symptom Checker"))
    st.info(t("This will be an ML-based symptom analysis form."))

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

