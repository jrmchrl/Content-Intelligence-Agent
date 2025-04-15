import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/Writer/palmyra-base"

def generate_geo_blueprint(topic):
    prompt = f"""
Du bist ein generativer SEO-Agent. Analysiere das Thema '{topic}' wie folgt:

1. Was ist die typische Suchintention hinter diesem Begriff?
2. Welche Longtail-Suchanfragen, Fragen und verwandte Themen sind relevant?
3. Welche Struktur könnte ein herausragender Blogpost zu diesem Thema haben?
4. Erstelle 2 alternative SEO-optimierte Headlines (z. B. emotional vs. sachlich).
5. Erstelle 2 passende Meta-Beschreibungen.
6. Bonus: Schreibe einen möglichen Einstiegstext für das Intro.
"""

    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 500}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Fehler: {response.status_code} - {response.json()}"