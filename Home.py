import streamlit as st
import config

# Configuration de la page Streamlit
st.set_page_config(page_title="Coursia", page_icon="assets/logo_coursia.png", layout="wide")

# Affichage du menu et de la barre du haut
config.init_session_state()
config.show_sidebar()

# Ajouter un pied de page
st.markdown("---")
st.markdown("👨‍💻 COURSIA - 2025 by RaynhCoding | Développé avec ❤️ et Streamlit")