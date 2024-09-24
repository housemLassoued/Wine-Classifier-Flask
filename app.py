from flask import Flask, request, render_template, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)

# Charger le modèle
model = joblib.load('model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    # Récupérer les données du formulaire
    data = []
    for i in range(len(request.form.getlist('fixed_acidity'))):
        row = {
            'fixed_acidity': float(request.form.getlist('fixed_acidity')[i]),
            'volatile_acidity': float(request.form.getlist('volatile_acidity')[i]),
            'citric_acid': float(request.form.getlist('citric_acid')[i]),
            'residual_sugar': float(request.form.getlist('residual_sugar')[i]),
            'chlorides': float(request.form.getlist('chlorides')[i]),
            'free_sulfur_dioxide': float(request.form.getlist('free_sulfur_dioxide')[i]),
            'total_sulfur_dioxide': float(request.form.getlist('total_sulfur_dioxide')[i]),
            'density': float(request.form.getlist('density')[i]),
            'pH': float(request.form.getlist('pH')[i]),
            'sulphates': float(request.form.getlist('sulphates')[i]),
            'alcohol': float(request.form.getlist('alcohol')[i]),
            'quality': int(request.form.getlist('quality')[i])
        }
        data.append(row)

    # Convertir les données en DataFrame
    df = pd.DataFrame(data)

    # Effectuer la prédiction pour toutes les lignes
    predictions = model.predict(df)

    # Ajouter les résultats de la classification à la DataFrame
    df['classe'] = ['white' if pred == 1 else 'red' for pred in predictions]

    # Retourner les résultats au template
    return render_template('index.html', data=df.to_dict(orient='records'))
if __name__ == '__main__':
    app.run(debug=True)