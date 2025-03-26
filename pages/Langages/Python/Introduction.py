import streamlit as st
import config 

config.init_session_state()

# Configuration de la page
st.set_page_config(page_title="Introduction à Python", page_icon="🤖", layout="wide")

# Afficher la barre du haut avec les boutons
config.show_top_bar()

# --- Contenu de la page ---
content = {
    "fr": {
        "title": "Introduction à Python",
        "intro": "Python est un langage de programmation de haut niveau, interprété et orienté objet. Il est simple à apprendre et à lire, ce qui en fait un excellent choix pour les débutants."
    },
    "en": {
        "title": "Introduction to Python",
        "intro": "Python is a high-level, interpreted, and object-oriented programming language. It is easy to learn and read, making it an excellent choice for beginners."
    }
}

lang = st.session_state.lang
st.title(content[lang]["title"])
st.write(content[lang]["intro"])