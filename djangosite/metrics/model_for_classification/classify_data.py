from sklearn.preprocessing import StandardScaler
from .load_model import load_model
from .constants import file_label_encoder, file_accuracy
from joblib import load


def classify_data(arr_data):
    scaler = StandardScaler()
    X = scaler.fit_transform(arr_data)
    model = load_model()
    label_encoder = load(file_label_encoder)
    accuracy = load(file_accuracy)
    result = label_encoder.inverse_transform(model.predict(X))
    return [result[0], f'RandomForestClassifier-based model with an accuracy of {accuracy}']
