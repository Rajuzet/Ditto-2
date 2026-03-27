def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)


def preprocess_data(data):
    # Example preprocessing steps
    # data = data.dropna()  # Remove missing values
    return data


def scale_features(data):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    return scaler.fit_transform(data)


def save_model(model, filename):
    import joblib
    joblib.dump(model, filename)


def load_model(filename):
    import joblib
    return joblib.load(filename)
