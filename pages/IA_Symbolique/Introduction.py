import streamlit as st

# Création des onglets
tabs = st.tabs(["Introduction"])

# Contenu de l'onglet "Introduction"
with tabs[0]:
    st.title("Introduction à l'IA Symbolique")
    st.markdown("""
    L'intelligence artificielle symbolique est une approche de l'intelligence artificielle qui traite des entités symboliques et des expressions de connaissance.
    Elle repose sur la manipulation de symboles et de règles logiques pour résoudre des problèmes.
    Les systèmes d'IA symbolique utilisent des modèles explicites de connaissances et des techniques de raisonnement pour effectuer des tâches intelligentes.
    """)

    st.header("Les principes de l'IA symbolique")
    principles = [
        "**Représentation symbolique** : les connaissances sont représentées sous forme de symboles, de concepts et de règles logiques.",
        "**Raisonnement symbolique** : les systèmes d'IA symbolique utilisent des règles logiques pour déduire de nouvelles informations.",
        "**Manipulation symbolique** : les symboles sont manipulés et combinés pour effectuer des opérations de raisonnement.",
        "**Interprétation symbolique** : les symboles sont interprétés et utilisés pour prendre des décisions ou effectuer des actions."
    ]
    for principle in principles:
        with st.container():
            st.markdown(f"- {principle}")

    st.header("Les applications de l'IA symbolique")
    applications = [
        "**Systèmes experts** : des systèmes capables de reproduire le raisonnement d'un expert humain.",
        "**Traitement automatique du langage naturel** : des systèmes capables de comprendre et de générer un langage naturel.",
        "**Planification et ordonnancement** : des systèmes capables de générer des plans d'action ou de résoudre des problèmes d'ordonnancement.",
        "**Représentation des connaissances** : des systèmes capables de représenter et de manipuler des connaissances complexes.",
        "**Raisonnement automatique** : des systèmes capables de déduire de nouvelles informations à partir de connaissances existantes."
    ]
    for application in applications:
        with st.container():
            st.markdown(f"- {application}")
