from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Chargement du modèle entraîné
model = joblib.load('imdb_model.pkl')

# Liste des fonctionnalités utilisées dans le modèle filtré
features_used = ['director_name', 'actor_2_name', 'genres', 'actor_1_name', 'movie_title', 'actor_3_name', 'content_rating', 'title_year', 'gross', 'budget', 'num_critic_for_reviews', 'duration', 'director_fb_likes', 'actor_3_fb_likes', 'actor_1_fb_likes', 'num_voted_users', 'cast_total_fb_likes', 'facenumber_in_poster', 'num_user_for_reviews', 'actor_2_fb_likes', 'movie_fb_likes']

@app.route('/')
def index():
    return render_template('form.html', features=features_used)

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données saisies par l'utilisateur depuis le formulaire
    input_data = {}
    for feature in features_used:
        input_data[feature] = request.form[feature]
    
    # Utiliser ces données pour faire une prédiction
    prediction = make_prediction(input_data)
    
    # Retourner la prédiction
    return jsonify({'prediction': prediction})

def make_prediction(input_data):
    # Créer un DataFrame avec les données saisies par l'utilisateur
    input_df = pd.DataFrame(input_data, index=[0])
    
    # Faire la prédiction avec le modèle chargé
    prediction = model.predict(input_df)
    
    return prediction[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
