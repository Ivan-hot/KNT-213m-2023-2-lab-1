from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from json import dumps


class TimeStampsViewTest(APITestCase):
    def test_timestamps_post(self):
        data = [{
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
                }
            ],
            "date": "2023-11-28",
            "time": "12:07:17"
        }]
        response = self.client.post(
            '/api/timestamps', dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
