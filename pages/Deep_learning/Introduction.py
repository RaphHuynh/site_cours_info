import streamlit as st

tabs = st.tabs(["Introduction"])

with tabs[0]:
    st.title("Introduction au Deep Learning")
    
    st.markdown("""
    L'apprentissage profond ou deep learning est une sous catégorie du machine learning. Il se concentre sur l'apprentissage de représentations de données complexes ou non structurées comme des images, des textes ou des sons. Pour cela, on va utiliser des réseaux de neurones artificiels pour apprendre aux différents modèles à traiter ces données.

    Il s'inspire du fonctionnement du cerveau humain pour apprendre à partir de données non structurées.
    
    ## Qu'est ce qu'un neurone ?
    
    Un neurone ou perceptron permet de simuler le fonctionnement des neurones biologiques du cerveau.

    Le neurone va recevoir des entrées de données qui sont des valeurs numériques qui représentent différentes caractéristiques ou variables. Chaque entrée possède un "poids" qui représente son importance pour le neurone.

    Les poids sont des coefficients (des valeurs) qui vont modifier l'importance de chaque entrées. Un poids élevé signifie que l'entrée est plus importante tandis qu'un poids faible sera moins important et aura donc moins d'impacte. Les poids sont ajustés au fur et à mesure de l'entrainement du modèle.

    En plus des poids il y a aussi les biais. En effet, un neurone possède un biais. Le biais est une constante elle permet de contrôler la sortie même quand les entrées sont nulles. Effectivement, contrairement au poids du neurones le biais permet de contrôler ce qu'on appelle le niveau d'activiation du neurone.

    En résumé un neurone possède une entrée, un poids, un biais aussi appelé seuil et une sortie.

    Une entrée c'est la donnée qui entre dans le neurone.
    
    ## Qu'est ce qu'un réseau de neurones ?
    
    Les réseaux de neurones sont des modèles composés de plusieurs couches de neurones qui sont interconnectées. Chaque couche va traiter via ses neurones les données entrantes et extraire des caractéristiques de ces données au fur et à mesure de l'entrainement.
    
    Il existe plusieurs types de réseaux de neurones, les plus connus sont les réseaux de neurones denses, les réseaux de neurones convolutifs et les réseaux de neurones récurrents.
    """)
    
    