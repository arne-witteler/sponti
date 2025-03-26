# app.py
import streamlit as st

st.title("Meine erste Streamlit-App 🎉")

st.write("Hallo! Das ist eine einfache Web-App mit Streamlit.")

name = st.text_input("Wie heißt du?")
if name:
    st.write(f"Schön, dich zu sehen, {name}!")