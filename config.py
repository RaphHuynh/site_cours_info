import streamlit as st

def init_session_state():
    """ Initialise les variables globales si elles n'existent pas encore. """
    if "lang" not in st.session_state:
        st.session_state.lang = "fr"  # Français par défaut
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False  # Mode clair par défaut

def apply_theme():
    """ Applique le thème choisi (clair ou sombre) avec CSS. """
    dark_style = """
    <style>
    body { background-color: #1E1E1E; color: white; }
    .stButton>button { background-color: #444; color: white; border-radius: 10px; }
    </style>
    """
    
    light_style = """
    <style>
    body { background-color: white; color: black; }
    .stButton>button { background-color: #ddd; color: black; border-radius: 10px; }
    </style>
    """

    st.markdown(dark_style if st.session_state.dark_mode else light_style, unsafe_allow_html=True)

def show_top_bar():
    """ Affiche la barre en haut avec les boutons de langue et de thème. """
    content = {
        "fr": {"lang_switch": "🇬🇧 English", "theme_switch": "🌙 / ☀️"},
        "en": {"lang_switch": "🇫🇷 Français", "theme_switch": "🌙 / ☀️"}
    }

    col1, col2, col3 = st.columns([8, 1, 1])  # Pour aligner les boutons à droite

    with col2:
        if st.button(content[st.session_state.lang]["lang_switch"]):
            st.session_state.lang = "en" if st.session_state.lang == "fr" else "fr"

    with col3:
        st.session_state.dark_mode = st.toggle(content[st.session_state.lang]["theme_switch"], value=st.session_state.dark_mode)

    apply_theme()  # Applique le thème après le choix


