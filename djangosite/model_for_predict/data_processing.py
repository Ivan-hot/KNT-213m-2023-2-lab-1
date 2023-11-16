import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib


def data_processing(filename):
    column_to_read = ['temp',
                      'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'wind_deg', 'rain_1h', 'snow_1h', 'clouds_all', 'weather_main']
    data = pd.read_csv(filename, usecols=column_to_read)

    data = data.fillna(0)

    # Кодування категоріальних ознак (weather_main) за допомогою Label Encoding
    label_encoder = LabelEncoder()
    data['weather_main'] = label_encoder.fit_transform(data['weather_main'])

    joblib.dump(label_encoder, 'label_encoder.joblib')

    X = data.drop('weather_main', axis=1)
    Y = data['weather_main']

    # standartization
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)

    return X_train, X_test, Y_train, Y_test
