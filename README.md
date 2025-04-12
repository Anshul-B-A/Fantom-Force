# 🚀 MammoMate

**Team Name:** _FantomForce_  
**Hackathon:** _FantomCode 2025_  
**Date:** _12/04/2025_

---

## 📖 Table of Contents

1. [Introduction](#-introduction)
2. [Problem Statement](#-problem-statement)
3. [Solution Overview](#-solution-overview)
4. [Tech Stack](#-tech-stack)
5. [Architecture / Diagram (if any)](#-architecture--diagram-if-any)
6. [Installation & Usage](#-installation--usage)
7. [Team Members](#-team-members)

---

## 🧠 Introduction

**MammoMate** is an AI-powered breast cancer awareness and support app designed especially for women in India. It offers tools to self-examine, track symptoms, access curated health content in regional languages, and engage with a supportive community — all in one place. MammoMate strives to empower early detection, informed decision-making, and emotional resilience through multilingual GenAI.

---

## ❗ Problem Statement

Breast cancer awareness in India remains alarmingly low — especially in rural and regional populations. Early detection can significantly reduce fatality rates, yet cultural stigma, language barriers, and lack of access to verified health resources delay diagnosis. There’s a pressing need for a private, accessible, tech-assisted companion to raise awareness and assist users in taking early action.

---

## ✅ Solution Overview

MammoMate addresses these issues with an all-in-one platform offering:

- 🤖 **GenAI-powered multilingual chatbot** (English, Hindi, Kannada, Malayalam)
- 🩺 **ML-based self-exam and symptom checker**  
- 🗺️ **Nearby hospital locator** using GIS
- 🗣️ **Community discussion forum** for peer support  
- 📄 **Auto-summarized educational articles** with TTS  
- 🔔 **Reminders for regular breast self-examinations**

All features are available even in guest mode, ensuring accessibility without the friction of sign-ups.

---

## 🛠️ Tech Stack

- **Frontend:** _Streamlit_
- **Backend:** _Python (Streamlit server)_
- **Database:** _Supabase (PostgreSQL-based)_
- **APIs / Libraries:** 
  - _Groq API (LLM for chatbot and summarization)_
  - _Google Maps API (hospital locator)_
  - _PyMuPDF (PDF text extraction)_
  - _Tesseract OCR (image-based text extraction)_
  - _Matplotlib & Seaborn (data visualization)_
  - _Pandas (data manipulation)_
- **Tools:** _GitHub, Figma, Python-dotenv_

---

## 🧩 Architecture / Diagram (if any)


<img width="1442" alt="Screenshot 2025-04-05 at 4 50 10 AM" src="https://github.com/user-attachments/assets/5e63080c-0b89-4059-a972-2c853176e61b" />
  
*Modular structure with language translation, AI chat, symptom checker, and community forum, all routed via Streamlit.*

---

## 🧪 Installation & Usage

### Prerequisites

- Python 3.9+
- A `.env` file and '.toml' file with keys for:
  - `GROQ_API_KEY`
  - `SUPABASE_URL`
  - `SUPABASE_KEY`
  - `GOOGLE_MAPS_API_KEY`

### Steps

```bash
# Clone the repository
git clone https://github.com/your-repo-url.git

# Navigate into the project directory
cd MammoMate

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r [requirements.txt](http://_vscodecontentref_/0)

# Run the app
streamlit run [dashboard.py](http://_vscodecontentref_/1)

