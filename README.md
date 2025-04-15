# 🧠 Content Intelligence Agent

Ein einfaches AI-Tool zur Textanalyse mit Hugging Face und Streamlit.  
Es verwendet ein Sentiment-Analyse-Modell, um Texte automatisch zu bewerten.

## 🚀 Tech Stack
- Hugging Face Inference API
- Streamlit für UI
- Python & Requests

## 🔍 Beispiel-Model:
[distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)

Dieses Modell kann zur Klassifikation von Themen verwendet werden. Das rohe Modell kann entweder für Masked Language Modellierung oder die Vorhersage des nächsten Satzes verwendet werden, sollte aber hauptsächlich für eine nachgelagerte Aufgabe feinjustiert werden. 


## 🔁 Zusatz-Module dieses Agenten:
- [ ] Zusatz-Modul: GEO-Agent 
        KI-Agent, der Inhalte nicht nur für Suchmaschinen optimiert,
        sondern mit KI erzeugt, semantisch klüger ist und auf Suchintentionen reagiert.

        Statt:“Gib mir Keywords zu ‘Nachhaltige Möbel’” → „nachhaltig“, „ökologisch“, „Design“
        Macht GEO: “Versteh das Thema, erfasse Suchintentionen, bau Inhalte, die Menschen und Suchmaschinen abholen.”

- [ ] Medienanalyse aus PDF oder HTML (→ nächstes Level)
- [ ] Streamlit bei Hugging Face Spaces oder Streamlit Cloud deployen


## 🧪 Testen
```bash
streamlit run app.py