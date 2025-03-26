import streamlit as st
import config 
import menu

# Configuration de la page Streamlit
st.set_page_config(page_title="Apprendre l'IA et les interfaces", page_icon="🤖", layout="wide")

# Affichage du menu et de la barre du haut
menu.show_sidebar()
config.init_session_state()
config.show_top_bar()

# --- Contenu de la page ---
content = {
    "fr": {
        "title": "👋 Bienvenue sur la plateforme d'apprentissage IA & Interfaces",
        "intro": (
            "Bienvenue sur cette plateforme dédiée à l'apprentissage de l'Intelligence Artificielle et de la création "
            "d'interfaces interactives. Vous allez découvrir et maîtriser des concepts clés de l'IA en utilisant les "
            "langages Python et R, et apprendre à concevoir des applications interactives à l'aide de Streamlit et Shiny.\n\n"
            
            "Ce site est organisé en différentes sections afin de vous guider à travers les étapes essentielles :\n\n"
            
            "- **Machine Learning (Apprentissage Automatique)** : Découvrez les bases de l'apprentissage supervisé et "
            "non supervisé, avec des applications dans la classification, le clustering, et bien plus encore.\n\n"
            
            "- **Deep Learning (Apprentissage Profond)** : Explorez les réseaux de neurones, les CNN, les transformers "
            "et apprenez à construire des modèles de deep learning puissants.\n\n"
            
            "- **IA Symbolique** : Plongez dans les concepts de l'IA basée sur la logique et les systèmes experts.\n\n"
            
            "- **Bases de Données** : Apprenez à interagir avec les bases de données SQL et NoSQL, en utilisant MySQL, "
            "MongoDB, et plus encore.\n\n"
            
            "- **Interfaces interactives** : Découvrez comment créer des applications interactives avec Streamlit et Shiny, "
            "pour rendre vos projets d'IA plus accessibles et interactifs.\n\n"
            
            "Ce site vous accompagnera à travers des projets pratiques et des exemples concrets pour que vous puissiez "
            "rapidement appliquer ce que vous apprenez à des cas réels.\n\n"
            
            "En suivant ce parcours, vous allez :\n\n"
            
            "- Acquérir des compétences techniques solides en IA et en développement d'interfaces interactives.\n"
            "- Maîtriser les outils les plus utilisés dans l'IA.\n"
            "- Être capable de créer des applications complètes alliant IA et interfaces interactives."
        ),
    },
    "en": {
        "title": "👋 Welcome to the AI & Interfaces Learning Platform",
        "intro": (
            "Welcome to this platform dedicated to learning Artificial Intelligence and creating interactive interfaces. "
            "You will discover and master key AI concepts using Python and R, and learn how to build interactive apps using "
            "Streamlit and Shiny.\n\n"
            
            "This site is organized into different sections to guide you through the essential steps:\n\n"
            
            "- **Machine Learning**: Discover the fundamentals of supervised and unsupervised learning, with applications in "
            "classification, clustering, and more.\n\n"
            
            "- **Deep Learning**: Explore neural networks, CNNs, transformers, and learn how to build powerful deep learning models.\n\n"
            
            "- **Symbolic AI**: Dive into concepts of logic-based AI and expert systems.\n\n"
            
            "- **Databases**: Learn how to interact with SQL and NoSQL databases, using MySQL, MongoDB, and more.\n\n"
            
            "- **Interactive Interfaces**: Learn how to build interactive apps with Streamlit and Shiny, making your AI projects "
            "more accessible and interactive.\n\n"
            
            "This site will guide you through hands-on projects and concrete examples, so you can quickly apply what you learn "
            "to real-world cases.\n\n"
            
            "By following this path, you will:\n\n"
            
            "- Gain solid technical skills in AI and interactive interface development.\n"
            "- Master the most widely used tools in AI.\n"
            "- Be able to create complete apps that combine AI and interactive interfaces."
        ),
    }
}

# Afficher le contenu selon la langue sélectionnée
lang = st.session_state.lang
st.title(content[lang]["title"])
st.markdown(content[lang]["intro"])
