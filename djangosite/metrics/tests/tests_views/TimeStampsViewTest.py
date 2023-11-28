from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class TimeStampsViewTest(TestCase):
    def test_timestamps_post(self):
        data = {
            "location": {
                "name": "Washington",
                "latitude": "47.751076N",
                "longitude": "120.740135W"
            },
            "measurement": [
                {
                    "name": "temp",
                    "description": "The Temperature refers to the actual temperature at a specific location or time",
                    "unit": "Kelvin",
                    "value": 272.67
                },
                {
                    "name": "feels_like",
                    "description": "Temperature Feels Like represents the perceived temperature, which may vary from the actual temperature due to factors like humidity and wind.",
                    "unit": "Kelvin"
                },
                {
                    "name": "temp_min",
                    "description": "Temperature Min signifies the minimum temperature recorded within a specific period, providing insights into the coldest conditions.",
                    "unit": "Kelvin",
                    "value": 272.67
                },
                {
                    "name": "temp_max",
                    "description": "Temperature Max indicates the maximum temperature observed within a specific timeframe, offering information about the warmest conditions.",
                    "unit": "Kelvin",
                    "value": 272.67
                },
                {
                    "name": "pressure",
                    "description": "Pressure refers to the atmospheric pressure at sea level, representing the force exerted by the air molecules in the atmosphere.",
                    "unit": "hPa",
                    "value": 1029
                },
                {
                    "name": "humidity",
                    "description": "Humidity indicates the amount of water vapor present in the air, expressed as a percentage. It reflects the air's moisture content.",
                    "unit": "%",
                    "value": 76
                },
                {
                    "name": "wind_speed",
                    "description": "Wind Speed represents the rate at which air is moving horizontally. It provides information about how fast the wind is blowing.",
                    "unit": "meter/sec",
                    "value": 1.06
                },
                {
                    "name": "wind_deg",
                    "description": "Wind Direction indicates the compass direction from which the wind is blowing. It provides insights into the orientation of the wind.",
                    "unit": "degrees",
                    "value": 317
                },
                {
                    "name": "rain_1h",
                    "description": "Rain_1h represents the amount of rainfall recorded in the last hour.",
                    "unit": "mm/h",
                    "value": 0
                },
                {
                    "name": "snow_1h",
                    "description": "Snow_1h indicates the amount of snowfall observed in the last hour.",
                    "unit": "mm/h",
                    "value": 0
                },
                {
                    "name": "clouds_all",
                    "description": "Clouds_All refers to the percentage of the sky covered by clouds, indicating the extent of cloud coverage.",
                    "unit": "%",
                    "value": 57
                },
                {
                    "name": "weather_main",
                    "description": "Weather_Main represents the main weather condition or category, such as Clear, Clouds, Rain, etc. It provides a general description of the current weather.",
                    "unit": "degrees",
                    "value": "Clouds"
                }
            ],
            "date": "2023-11-28",
            "time": "12:07:17"
        }
        response = self.client.post('/api/timestamps', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
