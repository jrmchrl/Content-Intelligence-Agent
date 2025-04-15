import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def generate_seo_content(topic):
    prompt = f"""
Du bist ein erfahrener deutschsprachiger SEO-Texter. Erstelle zum Thema '{topic}' einen vollständigen Content Blueprint:

1. 5 relevante SEO-Keywords
2. Vorschlag für eine Blogstruktur (Einleitung, 3 Abschnitte, Fazit)
3. Eine starke, klickstarke Headline
4. 3 weitere alternative Headlines mit Fokus auf Suchintention
5. Eine einleitende Textpassage (ca. 3 Sätze)

Antwort bitte direkt im Stil eines Content-Briefs.
"""
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300
        }
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Fehler: {response.status_code} - {response.json()}"