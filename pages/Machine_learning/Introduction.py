import streamlit as st

from pages.Machine_learning.cluster import introduction


# Créer des onglets
tab1, tab2 = st.tabs(["Introduction", "Cluster"])

# Onglet Introduction
with tab1:
    # Titre principal
    st.title("Introduction au Machine Learning")

    # Introduction
    st.markdown(
        """
        Le **Machine Learning**, ou **apprentissage automatique**, est un sous-domaine de l’**intelligence artificielle** qui repose sur des approches **mathématiques et statistiques**. 
        Son objectif est de permettre aux ordinateurs **d’apprendre à partir des données** afin d’exécuter des tâches sans être explicitement programmés.\n
        Le Machine Learning est utilisé dans de nombreux domaines, tels que la reconnaissance d’images, le traitement du langage naturel, 
        les systèmes de recommandation ou encore la détection de fraudes.
        """
    )

    # Section : Principaux problèmes du Machine Learning
    st.header("Les principaux problèmes du Machine Learning")

    st.markdown("Il existe plusieurs approches d'apprentissage en Machine Learning :")

    problems = {
        "Classification": "Attribuer une catégorie à une donnée en fonction de ses caractéristiques. Exemples : "
                          "classer des e-mails en spam ou non-spam, reconnaître des chiffres manuscrits, "
                          "détecter des avis positifs ou négatifs sur un produit.",
        
        "Régression": "Prédire une valeur numérique continue à partir de données d’entrée. Exemples : "
                      "estimer le prix d’un bien immobilier en fonction de sa surface et de sa localisation, "
                      "prédire la consommation d’énergie d’un bâtiment en fonction de la température extérieure.",
        
        "Clustering": "Regrouper des données similaires sans étiquettes préalablement définies. Exemples : "
                      "segmenter des clients en fonction de leur comportement d’achat, regrouper des documents "
                      "par thématique, identifier des communautés sur un réseau social.",
        
        "Séries temporelles": "Analyser des données qui évoluent dans le temps et prévoir leurs valeurs futures. "
                              "Exemples : prédictions météorologiques, estimation du trafic routier, "
                              "prévisions de ventes pour un produit.",
        
        "Réduction de dimension": "Simplifier un jeu de données tout en conservant l’essentiel des informations. "
                                  "Exemples : compresser des images tout en maintenant leur qualité, "
                                  "visualiser en 2D des données ayant de nombreuses variables, "
                                  "réduire le nombre de caractéristiques d’un modèle d’apprentissage."
    }

    for key, value in problems.items():
        st.markdown(f"- **{key}** : {value}")

    # Section : Différentes approches d’apprentissage
    st.header("Les différentes approches d’apprentissage")

    st.markdown("Le Machine Learning permet de répondre à plusieurs types de problèmes :")

    approaches = [
        {
            "title": "Apprentissage supervisé",
            "description": "L’algorithme apprend à partir de données étiquetées, c’est-à-dire des exemples pour lesquels la sortie correcte est connue.",
            "example": "Prédire si un patient est malade ou non à partir de ses symptômes.",
            "color": "#2A9D8F"
        },
        {
            "title": "Apprentissage non supervisé",
            "description": "L’algorithme est entraîné sur des données non étiquetées et doit identifier des structures sous-jacentes dans celles-ci.",
            "example": "Regrouper des clients ayant des comportements d’achat similaires.",
            "color": "#E76F51"
        },
        {
            "title": "Apprentissage semi-supervisé",
            "description": "Ce type d’apprentissage combine données étiquetées et non étiquetées pour améliorer la performance tout en réduisant le coût d’annotation.",
            "example": "Entraîner un modèle de reconnaissance faciale avec un faible nombre de visages identifiés.",
            "color": "#F4A261"
        },
        {
            "title": "Apprentissage auto-supervisé",
            "description": "L’algorithme génère lui-même des étiquettes à partir des données brutes et apprend sans supervision humaine.",
            "example": "Un modèle entraîné à prédire des mots manquants dans une phrase.",
            "color": "#264653"
        }
    ]

    cols = st.columns(len(approaches))
    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"""
                <div style="background-color: {approaches[i]['color']}; color: white; padding: 15px; border-radius: 10px; text-align: center; height: 300px; align-items: center; justify-content: center; display: flex; flex-direction: column;">
                    <p style="font-size: 1.2em; font-weight: bold;">{approaches[i]['title']}</p>
                    <p style="font-size: 0.9em;">{approaches[i]['description']}</p>
                    <p style="font-style: italic;">{approaches[i]['example']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Section : Types de données en Machine Learning
    st.header("📂 Types de données utilisées en Machine Learning")

    data_types = [
        "Vecteurs de caractéristiques : représentations numériques des données sous forme de variables.",
        "Graphes : structures relationnelles utilisées en analyse de réseaux sociaux ou en cybersécurité.",
        "Arbres : modèles hiérarchiques utilisés pour la prise de décision (ex. : arbres de décision).",
        "Séries temporelles : données évoluant dans le temps, utilisées en finance ou en météorologie."
    ]

    for item in data_types:
        st.markdown(f"- {item}")

# Onglet Cluster.py
with tab2:
    try:
        introduction.cluster_intro()
    except FileNotFoundError:
        st.error("Le fichier cluster.py est introuvable.")
