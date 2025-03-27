import streamlit as st
import config 

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