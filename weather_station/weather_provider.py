from datetime import datetime
import requests
import dto
from measurements import measurements
import urls


def get_weather_data(location) -> list[dto.Measurement] | None:
    weather_api = f'{urls.WEATHER_URL}?q={location["name"]}&appid={urls.API_KEY}'
    response = requests.get(weather_api)
    if response.status_code == 200:
        weather_data = response.json()
        measurements["temp"]["value"] = weather_data["main"]["temp"]
        measurements["feels_like"]["value"] = weather_data["main"]["feels_like"]
        measurements["temp_min"]["value"] = weather_data["main"]["temp"]
        measurements["temp_max"]["value"] = weather_data["main"]["temp"]
        measurements["pressure"]["value"] = weather_data["main"]["pressure"]
        measurements["humidity"]["value"] = weather_data["main"]["humidity"]
        measurements["wind_speed"]["value"] = weather_data["wind"]["speed"]
        measurements["wind_deg"]["value"] = weather_data["wind"]["deg"]
        measurements["rain_1h"]["value"] = weather_data["rain"]["1h"] if "rain" in weather_data else 0
        measurements["snow_1h"]["value"] = weather_data["snow"]["1h"] if "snow" in weather_data else 0
        measurements["clouds_all"]["value"] = weather_data["clouds"]["all"]
        measurements["weather_main"]["value"] = weather_data["weather"][0]["main"]

        measurement = list(measurements.values())
        cur_datetime = datetime.now()
        date = cur_datetime.date().strftime("%Y-%m-%d")
        time = cur_datetime.time().strftime("%H:%M:%S")
        timestamp = {"location": location,
                     "measurement": measurement, "date": date, "time": time}
        return timestamp
    else:
        return None
