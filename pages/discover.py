import streamlit as st

import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

# ------- Static Article Data (Easy to Copy-Paste) -------
articles = [
    {
        "title": "Breast Self-Examination Guide",
        "subtitle": "A step-by-step guide on how to perform breast self-examinations at home",
        "image": "assets/image_self_examination.jpg",
        "url": "https://www.breastcancer.org/screening-testing/breast-self-exam-bse"
    },
    {
        "title": "Understanding Mammograms",
        "subtitle": "What to expect during your mammogram and why they're important",
        "image": "assets/image_mammograms.jpg",
        "url": "https://www.fortishealthcare.com/blogs/understanding-mammograms-comprehensive-guide"
    },
    {
        "title": "Coping with Stress and Anxiety",
        "subtitle": "Recognizing and managing emotional challenges after a breast cancer diagnosis",
        "image": "assets/image_mental.jpg",
        "url": "https://breastcancernow.org/about-breast-cancer/life-after-treatment/coping-with-breast-cancer-emotionally/stress-and-anxiety-after-a-breast-cancer-diagnosis?utm_source=becca&utm_medium=web&utm_content=186"
    },
    {
        "title": "Managing Cancer-Related Fatigue",
        "subtitle": "Understand and cope with extreme tiredness during breast cancer treatment",
        "image": "assets/image_manage_fatigue.jpg",
        "url": "https://breastcancernow.org/about-breast-cancer/treatment/extreme-tiredness-cancer-related-fatigue?utm_source=becca&utm_medium=web&utm_content=1819"
    },
    {
        "title": "Maintaining Normalcy During Breast Cancer",
        "subtitle": "Yoga teacher Ruby Rubin shares how support and activities helped her stay grounded during treatment",
        "image": "assets/image_normalcy.jpg",
        "url": "https://www.healthline.com/health/breast-cancer/ask-the-advocate-maintaining-normalcy?utm_source=becca&utm_medium=web&utm_content=1972"
    },
    {
        "title": "Financial Support for Breast Cancer Patients",
        "subtitle": "Learn about benefits like universal credit, sick pay, and housing support during treatment",
        "image": "assets/image_finance.jpg",
        "url": "https://breastcancernow.org/about-breast-cancer/life-after-treatment/financial-support-and-benefits-when-you-have-breast-cancer?utm_source=becca&utm_medium=web&utm_content=1925"
    },
    {
        "title": "Managing Chemotherapy Side Effects",
        "subtitle": "Tips to cope with fatigue, nausea, and other common effects of cancer treatment",
        "image": "assets/image_chemo.jpg",
        "url": "https://www.everydayhealth.com/cancer/manage-side-effects-chemotherapy/?utm_source=becca&utm_medium=web&utm_content=1781"
    },
    {
        "title": "Diet Myths and Breast Cancer",
        "subtitle": "A dietician and nurse debunk myths, share tips for eating during and after treatment",
        "image": "assets/image_diet_myth.jpg",
        "url": "https://breastcancernow.org/about-us/podcasts/rav-diet-myths-and-recurrence-breast-cancer-now-podcast?utm_source=becca&utm_medium=web&utm_content=914"
    },
    {
        "title": "Leaning on Loved Ones During Treatment",
        "subtitle": "How to seek and accept support from family and friends during your breast cancer journey",
        "image": "assets/image_loved.jpg",
        "url": "https://www.healthline.com/health/breast-cancer/lean-on-loved-ones-during-treatment?utm_source=becca&utm_medium=web&utm_content=1931"
    }
]

# ------- Page UI -------
st.set_page_config(page_title="MammoMate Discover", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #d63384;'>MammoMate Community Articles</h1>",
    unsafe_allow_html=True
)

# Style for uniform card height

st.markdown("""
    <style>
        .article-card {
            background-color: #1e1e1e;
            border-radius: 12px;
            padding: 16px;
            height: 460px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            color: white;
            margin-bottom: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .article-card:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 20px rgba(255, 105, 180, 0.4);
        }

        .article-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 8px;
        }

        .article-title {
            font-size: 20px;
            margin-top: 10px;
            font-weight: bold;
        }

        .article-subtitle {
            font-size: 14px;
            color: #cccccc;
            margin-bottom: 10px;
        }

        .read-more-btn {
        background-color: #d63384;
        color: white !important;
        padding: 8px 14px;
        border: none;
        border-radius: 6px;
        text-decoration: none !important;
        text-align: center;
        display: inline-block;
        transition: all 0.3s ease;
        font-weight: 500;
    }

        .read-more-btn:hover {
            transform: scale(1.05);
            background-color: #e7549e;
            box-shadow: 0 0 10px rgba(255, 105, 180, 0.5);
            text-decoration: none;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --------- Render Cards ---------
cols = st.columns(3)

for i, article in enumerate(articles):
    img_src = get_base64_image(article["image"])
    with cols[i % 3]:
        st.markdown(f"""
            <div class="article-card">
                <img src="{img_src}" class="article-image" />
                <div class="article-title">{article['title']}</div>
                <div class="article-subtitle">{article['subtitle']}</div>
                <a href="{article['url']}" target="_blank" class="read-more-btn">Read More</a>
            </div>
        """, unsafe_allow_html=True)

