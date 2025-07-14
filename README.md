
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

### Technologies Utilisées

  * **Python**
  * **NumPy & Pandas** : Manipulation et analyse de données.
  * **SciPy** : Opérations sur les matrices creuses.
  * **`implicit` (ALS)** : Implémentation de l'algorithme Alternating Least Squares.
  * **Streamlit** : Création de l'interface utilisateur interactive.
  * **Matplotlib & Seaborn** : Visualisation de données.
  * **Azure Functions** : Hébergement de l'API de recommandation.
  * **GitHub Actions / Azure DevOps (potentiel)** : Pour le déploiement CI/CD.

### Structure du Projet

```
├── main.py               # Script principal d'entraînement et d'évaluation du modèle
├── app.py                # Application Streamlit pour l'interface utilisateur
├── azure_function/       # Dossier contenant le code de l'Azure Function
│   └── __init__.py
│   └── function.json
│   └── local.settings.json (IGNORÉ - pour développement local uniquement)
│   └── requirements.txt
├── data/
│   └── clicks_sample.csv # Exemple de données d'interaction utilisateur-article
├── .gitignore            # Fichiers et dossiers à ignorer par Git (inclut local.settings.json)
├── README.md             # Ce fichier
└── ...                   # Autres fichiers de configuration ou de support
```

### Démarrage Rapide

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/kriscillia-ai/reco-azure.git
    cd reco-azure
    ```
2.  **Installer les dépendances Python :**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Exécuter le script d'entraînement (localement) :**
    ```bash
    python main.py
    ```
4.  **Lancer l'application Streamlit (localement) :**
    ```bash
    streamlit run app.py
    ```
5.  **Déployer l'Azure Function (voir la documentation Azure Functions pour les étapes de déploiement).**
