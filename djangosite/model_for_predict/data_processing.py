import pandas as pd 
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

def data_processing(filename):
    # Вибираємо колонки, які будуть використовуватися
    columns_to_read = ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity', 'wind_speed', 'wind_deg', 'rain_1h', 'snow_1h', 'clouds_all', 'weather_main']
    
    # Зчитуємо дані з CSV-файлу, використовуючи лише вибрані колонки
    data = pd.read_csv(filename, usecols=columns_to_read)

    # Заповнюємо пропущені значення нулями
    data = data.fillna(0)

    # Кодуємо категоріальну ознаку 'weather_main' за допомогою Label Encoding
    label_encoder = LabelEncoder()
    data['weather_main'] = label_encoder.fit_transform(data['weather_main'])

    # Зберігаємо екземпляр LabelEncoder для подальшого використання при передачі нових даних
    joblib.dump(label_encoder, 'label_encoder.joblib')

    # Розділяємо дані на ознаки (X) та цільову змінну (Y)
    X = data.drop('weather_main', axis=1)
    Y = data['weather_main']

    # Стандартизуємо числові ознаки
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Розділяємо дані на тренувальний та тестовий набори
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Повертаємо результуючі дані для використання в моделі машинного навчання
    return X_train, X_test, Y_train, Y_test