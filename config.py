import streamlit as st

# Fonction pour initialiser les variables de session
def init_session_state():
    """ Initialise les variables globales si elles n'existent pas encore. """
    if "lang" not in st.session_state:
        st.session_state.lang = "fr"  # Français par défaut
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False  # Mode clair par défaut

# Fonction pour appliquer le thème choisi (clair ou sombre)
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

# Fonction pour afficher la barre latérale avec navigation
def show_sidebar():
    """ Affiche la barre latérale avec navigation dans Streamlit. """
    pg = st.navigation({
        "🤖 Machine Learning": [
            st.Page("pages/Machine_learning/Introduction.py", title="Introduction Machine Learning", url_path="ml-introduction"),
            st.Page("pages/Machine_learning/classification/introduction.py", title="Introduction à la classification", url_path="ml-classification-intro"),
            st.Page("pages/Machine_learning/cluster/introduction.py", title="Introduction au clustering", url_path="ml-clustering-intro"),
            st.Page("pages/Machine_learning/reduction_de_dimension/introduction.py", title="Introduction à la réduction de dimension", url_path="ml-dimension-reduction-intro"),
            st.Page("pages/Machine_learning/regression/introduction.py", title="Introduction à la régression", url_path="ml-regression-intro"),
        ],

        "🧠 Deep Learning": [
            st.Page("pages/Deep_learning/Introduction.py", title="Introduction au Deep Learning", url_path="dl-introduction"),
            st.Page("pages/Deep_learning/ANN.py", title="Réseaux de Neurones Artificiels", url_path="dl-ann"),
            st.Page("pages/Deep_learning/CNN.py", title="Réseaux de Neurones Convolutifs", url_path="dl-cnn"),
            st.Page("pages/Deep_learning/Transformers.py", title="Introduction aux Transformers", url_path="dl-transformers"),
        ],

        "♟️ IA Symbolique": [
            st.Page("pages/IA_Symbolique/Introduction.py", title="Introduction à l'IA Symbolique", url_path="ia-symbolique-introduction"),
            st.Page("pages/IA_Symbolique/Ingenierie_de_connaissance/Introduction.py", title="Ingénierie de connaissance", url_path="ia-symbolique-ingenierie"),
            st.Page("pages/IA_Symbolique/Systeme_Expert/Introduction.py", title="Systèmes experts", url_path="ia-symbolique-systeme-expert"),
        ],

        "🗄️ Bases de Données": [
            st.Page("pages/Base_de_données/SQL/Introduction.py", title="Introduction à SQL", url_path="sql-introduction"),
            st.Page("pages/Base_de_données/SQL/MySQL.py", title="Introduction à MySQL", url_path="mysql-introduction"),
            st.Page("pages/Base_de_données/SQL/PLSQL.py", title="Introduction à PL/SQL", url_path="plsql-introduction"),
            st.Page("pages/Base_de_données/SQL/SQLite.py", title="Introduction à SQLite", url_path="sqlite-introduction"),
            st.Page("pages/Base_de_données/NoSQL/Introduction.py", title="Introduction à NoSQL", url_path="nosql-introduction"),
            st.Page("pages/Base_de_données/NoSQL/MangoBD.py", title="Introduction à MongoDB", url_path="mongodb-introduction"),
        ],

        "🖥️ Interfaces": [
            st.Page("pages/Interfaces/Introduction.py", title="Introduction aux Interfaces", url_path="interfaces-introduction"),
            st.Page("pages/Interfaces/Shiny/Introduction.py", title="Introduction à Shiny (R)", url_path="shiny-introduction"),
            st.Page("pages/Interfaces/Streamlit/introduction.py", title="Introduction à Streamlit (Python)", url_path="streamlit-introduction"),
        ],

        "💻 Langages": [
            st.Page("pages/Langages/Python/Introduction.py", title="Introduction à Python", url_path="python-introduction"),
            st.Page("pages/Langages/R/Introduction.py", title="Introduction à R", url_path="r-introduction"),
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
        
        # Changer de mode (clair/sombre)
        st.session_state.dark_mode = st.toggle(content[st.session_state.lang]["theme_switch"], value=st.session_state.dark_mode)

    apply_theme()  # Applique le thème après le choix