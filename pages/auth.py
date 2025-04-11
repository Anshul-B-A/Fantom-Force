# pages/auth.py
import streamlit as st
from supabase import create_client, Client
import os
from utils.translation import t
from streamlit_lottie import st_lottie
import requests
import json

# Load particles Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

breast_cancer_anim = load_lottiefile("animations/breast_cancer.json")
st_lottie(breast_cancer_anim, speed=1, loop=True, quality="low", height=250, key="particle")

# --- Original auth page content below (unchanged) ---

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

if "lang" not in st.session_state:
    st.session_state.lang = "en"

lang = st.selectbox(
    label="🌐 Select Language",
    options=["English", "हिन्दी", "ಕನ್ನಡ", "മലയാളം"],
    index=["English", "हिन्दी", "ಕನ್ನಡ", "മലയാളം"].index("English")
)

lang_map = {
    "English": "en",
    "हिन्दी": "hi",
    "ಕನ್ನಡ": "kn",
    "മലയാളം": "ml"
}
st.session_state.lang = lang_map[lang]

st.title("🔐 " + t("login_title", st.session_state.lang))

auth_mode = st.radio(t("select_login_method", st.session_state.lang), [
    t("login", st.session_state.lang),
    t("continue_guest", st.session_state.lang)
])

if auth_mode == t("login", st.session_state.lang):
    email = st.text_input(t("email", st.session_state.lang))
    password = st.text_input(t("password", st.session_state.lang), type="password")

    if st.button(t("login_button", st.session_state.lang)):
        try:
            user = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            st.session_state["user"] = user
            st.success(t("login_success", st.session_state.lang))
            st.switch_page("pages/dashboard.py")
        except Exception as e:
            st.error(f"{t('login_failed', st.session_state.lang)}: {e}")

    st.markdown(t("signup_link", st.session_state.lang))

elif auth_mode == t("continue_guest", st.session_state.lang):
    if st.button(t("continue_guest", st.session_state.lang)):
        st.session_state["user"] = "guest"
        st.success(t("guest_success", st.session_state.lang))
        st.switch_page("pages/dashboard.py")
