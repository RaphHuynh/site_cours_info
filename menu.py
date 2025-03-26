import streamlit as st

def show_sidebar():
    """Affiche la barre latérale avec navigation dans Streamlit."""
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