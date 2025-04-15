import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

# Modellübersicht für verschiedene NLP-Tasks
MODELS = {
    "sentiment": "distilbert-base-uncased-finetuned-sst-2-english",
    "ner": "dslim/bert-base-NER",
    "topic": "facebook/bart-large-mnli",
    "keywords": "ml6team/keyphrase-extraction-distilbert-inspec",
    "qa": "deepset/roberta-base-squad2"
}

def run_model(model_key, inputs, additional_inputs=None):
    """
    Führt einen Hugging Face Inference API-Aufruf aus basierend auf dem gewählten Modell.
    :param model_key: Schlüsselwort wie 'sentiment', 'ner', 'topic', 'keywords', 'qa'
    :param inputs: Der Haupttext oder die Frage (bei QA)
    :param additional_inputs: Kontexttext für QA (optional)
    :return: JSON-Antwort vom Modell oder Fehlermeldung
    """
    model_url = f"https://api-inference.huggingface.co/models/{MODELS[model_key]}"

    # Spezieller Payload für Fragebeantwortung
    if model_key == "qa" and additional_inputs:
        payload = {
            "inputs": {
                "question": inputs,
                "context": additional_inputs
            }
        }
    else:
        payload = {"inputs": inputs}

    if model_key == "topic":
        payload["parameters"] = {
            "candidate_labels": [
                "Sport", "Politik", "Wirtschaft", "Technologie", "Kultur",
                "Wissenschaft", "Bildung", "Gesundheit", "Reisen", "Umwelt"
            ]
        }

    response = requests.post(model_url, headers=HEADERS, json=payload)

    try:
        return response.json()
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": response.text
        }