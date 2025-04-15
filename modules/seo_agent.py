import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def generate_seo_content(topic):
    prompt = f"""Erstelle einen SEO-Content-Plan zum Thema: {topic}.

Antwort in diesem Format:

- Relevante Keywords:
- Blogstruktur (Einleitung, 3 Abschnitte, Fazit):
- Haupt-Headline:
- 3 alternative Headlines:
- Einleitungstext (3 Sätze):
"""
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250
        }
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Fehler: {response.status_code} - {response.json()}"