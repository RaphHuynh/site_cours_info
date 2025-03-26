import streamlit as st
import config

# Configuration de la page Streamlit
st.set_page_config(page_title="Coursia", page_icon="assets/logo_coursia.png", layout="wide")

# Affichage du menu et de la barre du haut
config.init_session_state()
config.show_top_bar()
config.show_sidebar()

# --- Contenu de la page ---
content = {
    "fr": {
        "title": "👋 Bienvenue sur COURSIA",
        "intro": (
            "Cette plateforme est dédiée à l'apprentissage de l'informatique, de l'intelligence artificielle, de la data et "
            "d'interfaces interactives. Vous allez découvrir et maîtriser des concepts clés en utilisant les "
            "langages Python et R, et apprendre à concevoir des applications interactives à l'aide de Streamlit et Shiny.\n\n"
            "Ce site est organisé en différentes sections afin de vous guider à travers les étapes essentielles :\n\n"
        ),
        "autres": (
            "Ce site vous accompagnera à travers des projets pratiques et des exemples concrets pour que vous puissiez "
            "rapidement appliquer ce que vous apprenez à des cas réels.\n\n"
            "En suivant ce parcours, vous allez :\n\n"
            "- Acquérir des compétences techniques solides en IA et en développement d'interfaces interactives.\n"
            "- Maîtriser les outils les plus utilisés dans l'IA.\n"
            "- Être capable de créer des applications complètes alliant IA et interfaces interactives."
        )
    },
    "en": {
        "title": "👋 Welcome on COURSIA",
        "intro": (
            "This platform is dedicated to learning programming, artificial intelligence, data, and interactive interfaces."
            "You will discover and master key concepts using Python and R, and learn how to build interactive apps using "
            "Streamlit and Shiny.\n\n"
            "This site is organized into different sections to guide you through the essential steps:\n\n"
        ),
        "autres": (
            "This site will guide you through practical projects and real-world examples so you can quickly apply what you learn.\n\n"
            "By following this path, you will:\n\n"
            "- Acquire strong technical skills in AI and interactive interface development.\n"
            "- Master the most used tools in AI.\n"
            "- Be able to create complete applications combining AI and interactive interfaces."
        )
    }
}

st.title(content[st.session_state.lang]["title"])
st.markdown(content[st.session_state.lang]["intro"])

# Définir les titres et descriptions des cartes en fonction de la langue
cards = {
    "fr": [
        {"title": "Machine Learning", "description": "Découvrez les bases de l'apprentissage supervisé et non supervisé.", "color": "#F4A261"},
        {"title": "Deep Learning", "description": "Explorez les réseaux de neurones, CNNs, et transformers.", "color": "#2A9D8F"},
        {"title": "IA Symbolique", "description": "Plongez dans les concepts de l'IA basée sur la logique.", "color": "#E76F51"},
        {"title": "Bases de Données", "description": "Apprenez à interagir avec les bases de données SQL et NoSQL.", "color": "#264653"},
        {"title": "Interfaces interactives", "description": "Apprenez à créer des apps interactives avec Streamlit et Shiny.", "color": "#4FD1C5"},
    ],
    "en": [
        {"title": "Machine Learning", "description": "Discover the fundamentals of supervised and unsupervised learning.", "color": "#F4A261"},
        {"title": "Deep Learning", "description": "Explore neural networks, CNNs, and transformers.", "color": "#2A9D8F"},
        {"title": "Symbolic AI", "description": "Dive into the concepts of logic-based AI.", "color": "#E76F51"},
        {"title": "Databases", "description": "Learn how to interact with SQL and NoSQL databases.", "color": "#264653"},
        {"title": "Interactive Interfaces", "description": "Learn how to create interactive apps with Streamlit and Shiny.", "color": "#4FD1C5"},
    ]
}

# Affichage des cartes en fonction de la langue
cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
        <div style="background-color: {cards[st.session_state.lang][i]['color']}; color: white; padding: 10px; border-radius: 10px; height: 225px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <p style="font-size: 1.2em; margin: 0; padding: 0; font-weight: bold;">{cards[st.session_state.lang][i]['title']}</p>
            <p style="margin-top: 10px;">{cards[st.session_state.lang][i]['description']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("")
st.markdown(content[st.session_state.lang]["autres"])

# Ajouter un pied de page
st.markdown("---")
st.markdown("👨‍💻 COURSIA - 2025 | Développé avec ❤️ et Streamlit")

