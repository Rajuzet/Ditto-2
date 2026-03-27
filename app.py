from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the ML model
model = joblib.load('model.joblib')  # Make sure to update the path if needed

@app.route('/')
def home():
    return "Welcome to the ML Model Serving API!"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])  # Assuming features is a list
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)