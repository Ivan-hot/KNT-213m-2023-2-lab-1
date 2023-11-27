import pandas as pd
from .data_processing import data_processing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from .constants import *


def make_model():
    X_train, X_test, Y_train, Y_test = data_processing(
        file_data,  file_label_encoder)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, Y_train)

    Y_predict = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_predict)
    print(f'Accuracy: {accuracy*100}')

    joblib.dump(model,  file_model)
    joblib.dump(accuracy, file_accuracy)
    return True
