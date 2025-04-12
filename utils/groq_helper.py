import requests
import json

def stream_groq_chat(user_query, api_key, model="meta-llama/llama-4-scout-17b-16e-instruct"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You're a helpful breast cancer support assistant. Answer in a human friendly and informative manner. Always return answers as given in each user prompt."},
            {"role": "user", "content": user_query}
        ],
        "stream": True
    }

    response = requests.post(url, headers=headers, json=payload, stream=True)

    if response.status_code != 200:
        raise Exception(f"Groq API failed: {response.status_code} - {response.text}")

    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            if decoded_line.startswith("data: "):
                data_str = decoded_line.replace("data: ", "")
                if data_str != "[DONE]":
                    yield json.loads(data_str)["choices"][0]["delta"].get("content", "")


def summarize_with_groq(text, api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",  # 👈 or any from your screenshot
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that explains medical reports in simple words."
            },
            {
                "role": "user",
                "content": f"Please summarize and simplify this medical report:\n\n{text}"
            }
        ],
        "temperature": 0.3,
        "max_tokens": 1024
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        print("❌ API Error:", response.text)
        raise e
