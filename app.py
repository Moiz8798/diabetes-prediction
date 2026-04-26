from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler if they exist
model = None
scaler = None

def load_model():
    global model, scaler
    if os.path.exists('model.pkl') and os.path.exists('scaler.pkl'):
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        print("Model loaded successfully!")
    else:
        print("Model not found. Please run 'python diabetes_model.py' first.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded. Run diabetes_model.py first.'}), 500

    try:
        data = request.get_json()

        features = [
            float(data['pregnancies']),
            float(data['glucose']),
            float(data['blood_pressure']),
            float(data['skin_thickness']),
            float(data['insulin']),
            float(data['bmi']),
            float(data['dpf']),
            float(data['age'])
        ]

        features_array = np.array([features])
        features_scaled = scaler.transform(features_array)

        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]

        result = {
            'prediction': int(prediction),
            'label': 'Diabetic' if prediction == 1 else 'Not Diabetic',
            'confidence': round(float(max(probability)) * 100, 2),
            'diabetic_prob': round(float(probability[1]) * 100, 2),
            'healthy_prob': round(float(probability[0]) * 100, 2)
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    load_model()
    print("\n Starting server at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
