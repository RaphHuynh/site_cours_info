import streamlit as st

from pages.Guides_bonnes_pratiques.Computer_vision import Introduction

tab1, tab2 = st.tabs(["Introduction", "Computer Vision"])

with tab1:
    st.title("Introduction aux bonnes pratiques en programmation")
    
    st.markdown("Dans cette partie nous allons aborder les bonnes pratiques en programmation, en data science, computer vision, machine learning et autres.")
    
with tab2:
    try:
        Introduction.computer_vision_guide_intro()
    except Exception as e:
        st.error(f"Une erreur est survenue lors du chargement du guide Computer Vision : {e}")
        