import requests
import streamlit as st

def summarize_text(text):
    api_key = st.secrets["GROQ_API_KEY"]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-saba-24b",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that simplifies and summarizes medical reports in plain English."},
            {"role": "user", "content": f"Summarize and simplify this report:\n\n{text}"}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}\n\nRaw response: {response.text}"
