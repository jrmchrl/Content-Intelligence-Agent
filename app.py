from modules.geo_agent import generate_geo_blueprint

# neuer Tab
tab1, tab2, tab3 = st.tabs(["🔍 Medienanalyse", "✍️ SEO Generator", "🚀 GEO Agent"])

with tab3:
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