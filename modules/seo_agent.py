import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"

def generate_seo_content(topic):
    prompt = f"""
Du bist ein erfahrener deutschsprachiger SEO-Texter. Erstelle zum Thema '{topic}' einen vollständigen Content-Plan.

Format:

Relevante Keywords:
- ...

Blogstruktur:
- Einleitung
- Abschnitt 1
- Abschnitt 2
- Abschnitt 3
- Fazit

Haupt-Headline:
...

Alternative Headlines:
1. ...
2. ...
3. ...

Einleitungstext:
...
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
        return f"Fehler: {response.status_code} - {response.text}"