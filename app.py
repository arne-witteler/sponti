import streamlit as st

st.set_page_config(page_title="Sponti", page_icon="✨", layout="wide")

st.title("🎈 Finde spontane Aktivitäten")

# Session State für Auswahl speichern
if "altersgruppe" not in st.session_state:
    st.session_state["altersgruppe"] = None
if "zeit" not in st.session_state:
    st.session_state["zeit"] = None

with st.form("sponti_form"):
    st.subheader("🔎 Suche")

    # Standort
    standort = st.text_input("📍 Standort", placeholder="Adresse eingeben oder Standort freigeben")
    st.caption("Klicke auf das Standort-Icon, um deine aktuelle Position zu erkennen.")

    # Personenanzahl
    personen = st.slider("👥 Personenanzahl", min_value=1, max_value=20, value=2)

    # Altersgruppe Auswahl als Button-Reihe
    st.markdown("### 👤 Altersgruppe")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.form_submit_button("Kinder"):
            st.session_state["altersgruppe"] = "Kinder"
    with col2:
        if st.form_submit_button("Jugendliche"):
            st.session_state["altersgruppe"] = "Jugendliche"
    with col3:
        if st.form_submit_button("Erwachsene"):
            st.session_state["altersgruppe"] = "Erwachsene"

    # Zeitpräferenz Auswahl als Button-Reihe
    st.markdown("### 🕒 Zeitpräferenz")
    col4, col5 = st.columns(2)
    with col4:
        if st.form_submit_button("Heute"):
            st.session_state["zeit"] = "Heute"
    with col5:
        if st.form_submit_button("Morgen"):
            st.session_state["zeit"] = "Morgen"

    # Finaler Suchbutton
    submitted = st.form_submit_button("🚀 Aktivitäten finden")

# Ergebnisse anzeigen
if submitted:
    if not (standort and st.session_state["altersgruppe"] and st.session_state["zeit"]):
        st.error("Bitte gib Standort, Altersgruppe und Zeitpräferenz an.")
    else:
        st.success(f"🔍 Suche gestartet für {personen} {st.session_state['altersgruppe'].lower()} in {standort} – Zeit: {st.session_state['zeit']}")