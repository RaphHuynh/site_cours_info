import streamlit as st

# Fonction pour initialiser les variables de session
def init_session_state():
    """ Initialise les variables globales si elles n'existent pas encore. """
    if "lang" not in st.session_state:
        st.session_state.lang = "fr"  # Français par défaut

# Fonction pour afficher la barre latérale avec navigation
def show_sidebar():
    """ Affiche la barre latérale avec navigation dans Streamlit. """
    st.logo("assets/logo_coursia.png")

    pg = st.navigation({
        "Accueil": [
                st.Page("pages/Accueil.py",
                    title="Accueil" if st.session_state.lang == "en" else "Home",
                    url_path="home"),
        ],
        "🤖 Intelligence Artificielle / AI": [
                st.Page("pages/IA_Symbolique/Introduction.py", 
                    title="Symbolic AI " if st.session_state.lang == "en" else "IA Symbolique", 
                    url_path="ia-symbolique-introduction"),
                st.Page("pages/Machine_learning/Introduction.py", 
                    title="Machine Learning" if st.session_state.lang == "en" else "Machine Learning", 
                    url_path="ml-introduction"),
                st.Page("pages/Deep_learning/Introduction.py", 
                    title="Deep Learning" if st.session_state.lang == "en" else "Deep Learning", 
                    url_path="dl-introduction"),
        ],
        "🗄️ Databases": [

        ],

        "🖥️ Interfaces": [
        ],

        "💻 Programming Languages": [
                st.Page("pages/Langages/Python/Introduction.py", 
                    title="Python Introduction" if st.session_state.lang == "en" else "Python", 
                    url_path="python-introduction"),
        ],
    })

    pg.run()

# Fonction pour afficher la barre en haut avec les boutons de langue et de thème dans la sidebar
def show_top_bar():
    """ Affiche la barre en haut avec les boutons de langue et de thème. """
    content = {
        "fr": {"lang_switch": "🇬🇧 English", "theme_switch": "🌙 / ☀️"},
        "en": {"lang_switch": "🇫🇷 Français", "theme_switch": "🌙 / ☀️"}
    }

    with st.sidebar:
        # Changer de langue
        if st.button(content[st.session_state.lang]["lang_switch"]):
            st.session_state.lang = "en" if st.session_state.lang == "fr" else "fr"