
## Système de Recommandation d'Articles

Ce projet implémente un système de recommandation d'articles basé sur le **filtrage collaboratif** à l'aide de l'algorithme **Alternating Least Squares (ALS)**. Il est conçu pour suggérer des articles pertinents aux utilisateurs en analysant leurs interactions passées (clics) et celles d'utilisateurs similaires.

Le projet est structuré pour une intégration et un déploiement continus (CI/CD) sur Azure, avec une application Streamlit pour l'interface utilisateur.

### Fonctionnalités Clés

  * **Chargement et Préparation Avancée des Données** : Filtration des interactions rares pour assurer la qualité du modèle.
  * **Création de Matrice Creuse** : Transformation des interactions utilisateur-article en une matrice creuse optimisée pour l'entraînement ALS.
  * **Split Train-Test Temporel** : Division des données en ensembles d'entraînement et de test en respectant la chronologie des interactions.
  * **Entraînement du Modèle ALS** : Utilisation de l'algorithme Alternating Least Squares pour découvrir les facteurs latents des utilisateurs et des articles.
  * **Optimisation des Hyperparamètres** : Recherche des meilleurs paramètres pour le modèle ALS via une méthode de Grid Search.
  * **Génération de Recommandations Personnalisées** : Fonctionnalité pour recommander des articles à un utilisateur spécifique, avec option de filtrage des articles déjà consultés.
  * **Évaluation des Performances** : Mesure de la qualité des recommandations à l'aide du score Mean Average Precision (MAP@K).
  * **Visualisation des Facteurs Latents** : Analyse des représentations vectorielles des articles pour mieux comprendre les relations découvertes par le modèle.
  * **Déploiement sur Azure** : Intégration avec Azure Functions pour l'API de recommandation et une application Streamlit pour l'interface utilisateur.

### Démonstration du projet

<img width="608" height="122" alt="image" src="https://github.com/user-attachments/assets/eec4376c-4a67-4f4b-bb22-899cb9b40200" />

<img width="607" height="389" alt="image" src="https://github.com/user-attachments/assets/fd442b54-63fc-48fe-83d9-d34e797487ce" />


### Technologies Utilisées

  * **Python**
  * **NumPy & Pandas** : Manipulation et analyse de données.
  * **SciPy** : Opérations sur les matrices creuses.
  * **`implicit` (ALS)** : Implémentation de l'algorithme Alternating Least Squares.
  * **Streamlit** : Création de l'interface utilisateur interactive.
  * **Matplotlib & Seaborn** : Visualisation de données.
  * **Azure Functions** : Hébergement de l'API de recommandation.
  * **GitHub Actions / Azure DevOps (potentiel)** : Pour le déploiement CI/CD.

