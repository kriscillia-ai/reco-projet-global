import logging
import azure.functions as func
import pickle
import gzip
from io import BytesIO
import json
import numpy as np

# Encodeur JSON personnalisé pour gérer les types NumPy
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        return super().default(obj)

# Configuration de l'application avec niveau d'autorisation Anonymous
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="recommend", methods=["POST"])
@app.blob_input(
    arg_name="modelblob",
    path="appreco/best_als_model.pkl",
    connection="AzureWebJobsStorage",  # Utilisation de la chaîne de connexion principale
    data_type="binary"
)
def recommend(req: func.HttpRequest, modelblob: func.InputStream) -> func.HttpResponse:
    try:
        # Vérification du blob
        if not modelblob or not modelblob.readable():
            raise ValueError("Blob inaccessible")

        # Lecture et désérialisation
        blob_data = modelblob.read()
        try:
            with gzip.GzipFile(fileobj=BytesIO(blob_data), mode='rb') as f:
                model_data = pickle.load(f)
        except (gzip.BadGzipFile, OSError):
            model_data = pickle.loads(blob_data)

        # Validation renforcée
        required_keys = {'model', 'user_map', 'article_map', 'user_items'}
        if not all(key in model_data for key in required_keys):
            raise ValueError("Structure de modèle invalide")

        # Récupération de l'ID utilisateur
        user_input = req.get_json().get('user_id')
        if not user_input:
            return func.HttpResponse("ID utilisateur requis", status_code=400)

        # Conversion sécurisée en np.int64
        try:
            user_id = np.int64(int(user_input))
        except ValueError:
            return func.HttpResponse("Format ID invalide", status_code=400)

        # Recherche dans user_map
        user_map = model_data['user_map']
        if user_id not in user_map:
            return func.HttpResponse(f"ID {user_id} inconnu", status_code=404)

        user_idx = user_map[user_id]

        # Génération des recommandations
        ids, scores = model_data['model'].recommend(
            userid=user_idx,
            user_items=model_data['user_items'][user_idx],
            N=5,
            filter_already_liked_items=True
        )

        # Mapping des articles avec conversion de type
        inv_article_map = {v: k for k, v in model_data['article_map'].items()}
        recommendations = [
            {
                "article_id": str(inv_article_map[i]),  # Conversion en str
                "score": float(s)  # Conversion en float natif
            }
            for i, s in zip(ids, scores)
        ]

        # Réponse HTTP avec encodeur personnalisé
        return func.HttpResponse(
            json.dumps(
                {
                    "user_id": int(user_id),  # Conversion en int natif
                    "recommendations": recommendations
                },
                cls=NpEncoder  # Utilisation de l'encodeur personnalisé pour JSON
            ),
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Échec critique : {str(e)}", exc_info=True)
        return func.HttpResponse(
            f"Erreur de traitement : {str(e)}",
            status_code=500
        )
