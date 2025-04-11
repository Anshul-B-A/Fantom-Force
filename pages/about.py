import streamlit as st
from utils.translation import t

st.set_page_config(page_title=t("About Us"), page_icon="📖")

# Language selector
lang = st.selectbox("🌐 " + t("Choose Language"), options=["en", "kn", "ml"], format_func=lambda x: {"en": "English", "kn": "ಕನ್ನಡ", "ml": "മലയാളം"}[x])
st.session_state.lang = lang  # Store selected language globally

# Header
st.title(t("🎗️ About Us", lang))

# Story
st.markdown(f"""
{t("Breast cancer affects millions of women worldwide, and in India, it's the most common cancer among women. Many go undiagnosed due to lack of awareness, stigma, and access to timely care.", lang)}

{t("Our mission is to use AI and technology to support early detection, provide accessible information, and empower women with tools and knowledge in their own language.", lang)}

{t("This platform is built to reach both rural and urban populations, respecting linguistic diversity and supporting a variety of needs with empathy and innovation.", lang)}
""")

# Stats
st.subheader(t("📊 Key Statistics", lang))
st.markdown(f"""
- 📍 {t("In India, 1 in 28 women is likely to develop breast cancer during her lifetime.", lang)}
- 🌍 {t("Globally, over 2.3 million women were diagnosed with breast cancer in 2020.", lang)}
- ⏱️ {t("Early detection can improve survival rates by over 90%.", lang)}
""")

# Meet the Team
st.subheader(t("🤝 Meet Our Team", lang))
st.markdown(f"""
- **Anshul B A** – {t("A CSE undergrad passionate about healthcare innovation and building impactful technology.", lang)}
- **Gayathri Jayan** – {t("A driven developer with a heart for solving real-world problems through AI and design.", lang)}
""")

# Disclaimer
st.subheader(t("⚠️ Disclaimer", lang))
st.info(t("This platform is for informational and awareness purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified medical professional.", lang))

# Footer
st.markdown("---")
st.caption(t("© 2025 nariSaathi. All rights reserved.", lang))
