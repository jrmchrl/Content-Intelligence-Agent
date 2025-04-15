import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/gpt2"  # Oder anderes Textmodell

def generate_seo_content(topic):
    prompt = f"""
Du bist ein SEO-Texter. Für das Thema '{topic}':
1. Nenne 5 relevante Keywords
2. Skizziere eine Blogstruktur (Einleitung, 3 Abschnitte, Fazit)
3. Gib eine starke SEO-Headline aus
4. Nenne 3 alternative Headlines
"""
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 300}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Fehler: {response.status_code} - {response.json()}"