import streamlit as st

def computer_vision_guide_intro():
    st.title("Les bonnes pratiques en Computer Vision")
    
    st.markdown("""
    
    # Introduction

    Dans cette partie nous allons aborder les bonnes pratiques en Computer Vision. Nous allons commencer par voir les principes généraux en Computer Vision, puis nous aborderons les principes clés pour les approches dites classiques en computer vision. Puis, nous finirons par les bonnes pratiques pour les approches basées sur le Deep Learning.
    
    # Principes généraux en Computer Vision
    
    ## Comprendre le problème
    
    Il est important avant de commencer un projet de bien comprendre le problème ou de bien le définir si c'est un projet perso 🙂. Pour ce faire il faut :
    
    - **Définir la ou les tâches à réaliser** : est-ce de la détection de contour ? s'agit-il de suivre un mouvement ? d'analyser des couleurs ? de classifier des images ? de détecter ? de segmenter ? etc.
    
    - **Identifier les contraintes** : Il est primordiale d'identifier les contraintes pour mieux s'adapter et anticiper. Par exemple temps réel ou pas, matériel disponible, temps nécessaire, robustesse face aux variations des conditions réels (éclairages, bruitages , angles de vues, etc)

    - **Evaluer la faisabilité** : Il est important aussi avant de commencer un projet de savoir si le problème est réalisable avec les données et les ressources disponibles.

    """)