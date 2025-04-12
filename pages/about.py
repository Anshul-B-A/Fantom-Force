import streamlit as st
from utils.translation import t

st.set_page_config(page_title=t("About Us"), page_icon="🎗️")

# Language selector
lang = st.selectbox("🌐 " + t("Choose Language"), options=["en", "hi", "kn", "ml"], format_func=lambda x: {"en": "English", "hi": "हिन्दी", "kn": "ಕನ್ನಡ", "ml": "മലയാളം"}[x])


st.title(t("🎗️ About Us", lang))

# Introduction
st.markdown(f"""
{t("MammoMate is an AI-powered platform designed to raise awareness, support early detection, and offer multilingual guidance for breast cancer—especially in underserved communities.", lang)}

{t("Breast cancer is the most common cancer among women in India, yet many remain unaware or undiagnosed due to social stigma, lack of access, and language barriers. MammoMate is our solution to close this gap with empathy and innovation.", lang)}
""")

# Vision & Mission
st.subheader(t("🌟 Vision(Our Why) & Mission(Our What)", lang))
st.markdown(f"""
> 🧬 **{t("Vision", lang)}:** {t("By 2050, everyone diagnosed with breast cancer will live and be supported to live well.", lang)}

> 🎯 **{t("Mission", lang)}:** {t("To help people understand the complex medical and personal information about breast health, enabling them to make informed decisions and seek help without fear or stigma.", lang)}
""")

# Goals
st.subheader(t("🎯 Our Goals (Our How)", lang))
st.markdown(f"""
- ✅ {t("Stop people dying from breast cancer.", lang)}
- ✅ {t("Support people to live well with breast cancer.", lang)}
- ✅ {t("Accelerate detection using AI and modern techniques.", lang)}
- ✅ {t("Improve prevention through education and outreach.", lang)}
- ✅ {t("Empower rural and regional populations with multilingual access to life-saving information.", lang)}
""")

# Key Stats
st.subheader(t("📊 Key Statistics", lang))
st.markdown(f"""
- 📍 {t("In India, 1 in 28 women is likely to develop breast cancer during her lifetime.", lang)}  
  👉 [Source: National Cancer Registry Programme (ICMR)](https://ncdirindia.org/All_Reports/Report_2020/Default.aspx)

- 🌍 {t("Globally, over 2.3 million women were diagnosed with breast cancer in 2024.", lang)}  
  👉 [Source: WHO – Breast Cancer Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/breast-cancer)

- ⏱️ {t("Early detection can improve survival rates by over 90%.", lang)}  
  👉 [Source: American Cancer Society – Breast Cancer Early Detection](https://www.cancer.org/cancer/breast-cancer/screening-tests-and-early-detection.html)
""")


# Disclaimer
st.subheader(t("⚠️ Disclaimer", lang))
st.info(t("This platform is for informational and awareness purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified medical professional.", lang))

st.markdown("---")
# Meet the Team
#<--image correction function-->
from PIL import Image, ExifTags
import streamlit as st

def load_and_correct_image(path):
    image = Image.open(path)
    
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == "Orientation":
                break
        exif = dict(image._getexif().items())
        orientation_value = exif.get(orientation)

        if orientation_value == 3:
            image = image.rotate(180, expand=True)
        elif orientation_value == 6:
            image = image.rotate(270, expand=True)
        elif orientation_value == 8:
            image = image.rotate(90, expand=True)
    except Exception:
        pass  # No EXIF info or orientation tag

    return image
#<--image correction function end-->
st.subheader(t("🤝 Meet Our Team", lang))
st.markdown(t("We are two passionate students on a mission to democratize healthcare and make AI accessible to those who need it most.", lang))

cols = st.columns(2)
with cols[0]:
    corrected_image = load_and_correct_image("assets/image_anshul.jpg")
    st.image(corrected_image, use_container_width=True)


    st.markdown(f"""
    **Anshul B A**  
    _{t("Co-founder & Developer")}_  
    {t("A CSE undergrad passionate about healthcare innovation and building impactful technology.", lang)}
    """)
with cols[1]:
    corrected_image = load_and_correct_image("assets/image_gayathri.jpg")
    st.image(corrected_image, use_container_width=True)


    st.markdown(f"""
    **Gayathri Jayan**  
    _{t("Co-founder & Developer")}_  
    {t("A driven developer with a heart for solving real-world problems through AI and design.", lang)}
    """)


# Footer
st.markdown("---")
st.caption(t("© 2025 MammoMate. All rights reserved.", lang))
