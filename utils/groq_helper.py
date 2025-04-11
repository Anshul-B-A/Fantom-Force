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
            {"role": "system", "content": "You're a helpful breast cancer support assistant."},
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
