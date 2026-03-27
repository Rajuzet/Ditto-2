# Inference Script for ML Model

import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

# Function to run predictions

def run_inference(input_data):
    # Preprocess the input data if necessary
    # Assuming input_data is a list of features
    input_array = np.array(input_data).reshape(1, -1)  # Reshape for a single sample
    predictions = model.predict(input_array)
    return predictions

# Example usage:
if __name__ == '__main__':
    sample_input = [5.1, 3.5, 1.4, 0.2]  # Replace with actual feature values
    print(run_inference(sample_input))
