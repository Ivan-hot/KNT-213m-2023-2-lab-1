from datetime import datetime
import requests
from . import dto
from .measurements import measurements
from . import urls


def get_weather_data(location) -> list[dto.Measurement] | None:
    weather_api= f'{urls.WEATHER_URL}?q={location["name"]}&appid={urls.API_KEY}'
    response = requests.get(weather_api)
    if response.status_code == 200:
        weather_data = response.json()
        measurements["temp"]["value"] = weather_data["main"]["temp"]
        measurements["pressure"]["value"] = weather_data["main"]["pressure"]
        measurements["humidity"]["value"] = weather_data["main"]["humidity"]
        measurements["windSpeed"]["value"] = weather_data["wind"]["speed"]
        measurements["windDeg"]["value"] = weather_data["wind"]["deg"]
        measurements["visibility"]["value"] = weather_data["visibility"]
        measurement = list(measurements.values())
        cur_datetime = datetime.now()
        date= cur_datetime.date().strftime("%Y-%m-%d")
        time = cur_datetime.time().strftime("%H:%M:%S")
        timestamp={"location":location,"measurment":measurement,"date":date,"time":time}
        return timestamp
    else:
        return None



    