import streamlit as st
from hf_query import analyze_text
from modules.seo_agent import generate_seo_content
from modules.geo_agent import generate_geo_blueprint
from modules.nlp_tasks import run_model

option = st.radio("Wähle ein Modul:", ["🔍 Medienanalyse", "✍️ SEO Generator", "🚀 GEO Agent", "🧠 NLP Toolkit"])

if option == "🔍 Medienanalyse":
    # Medienanalyse-Logik
    st.subheader("Medienanalyse")
    user_input = st.text_area("Gib deinen Text ein:")

    if user_input:
        st.write("⏳ Anfrage läuft...")
        result = analyze_text(user_input)
        st.write("✅ Ergebnis:")
        st.json(result)

elif option == "✍️ SEO Generator":
    # SEO-Modul
    st.subheader("SEO Generator")
    topic = st.text_input("Thema eingeben:")

    if topic:
        with st.spinner("🔧 Generiere SEO-Ideen..."):
            seo_result = generate_seo_content(topic)
        st.text_area("📋 SEO-Vorschlag", seo_result, height=300)

elif option == "🚀 GEO Agent":
    # GEO-Agent-Modul
    st.subheader("Generative Engine Optimization")
    geo_topic = st.text_input("Gib ein Thema ein (z. B. 'nachhaltige Büromöbel'):")

    if geo_topic:
        with st.spinner("📡 GEO Agent generiert Inhalte..."):
            geo_result = generate_geo_blueprint(geo_topic)
        st.text_area("🔎 Ergebnis", geo_result, height=400)
        st.download_button(
            label="💾 Ergebnis als Markdown speichern",
            data=geo_result,
            file_name=f"GEO_{geo_topic.replace(' ', '_')}.md",
            mime="text/markdown"
        )

elif option == "🧠 NLP Toolkit":
    st.subheader("🔍 Wähle NLP-Modell")
    model_choice = st.selectbox("Modell wählen", [
        "Sentiment",
        "Themenklassifikation",
        "Named Entity Recognition",
        "Keyword Extraction",
        "Fragebeantwortung"
    ])

    input_text = st.text_area("📝 Eingabetext")

    if model_choice == "Fragebeantwortung":
        question = st.text_input("❓ Frage zum Text")

    if st.button("Analyse starten"):
        model_key = {
            "Sentiment": "sentiment",
            "Themenklassifikation": "topic",
            "Named Entity Recognition": "ner",
            "Keyword Extraction": "keywords",
            "Fragebeantwortung": "qa"
        }[model_choice]

        result = run_model(model_key, question if model_key == "qa" else input_text, input_text if model_key == "qa" else None)
        st.json(result)