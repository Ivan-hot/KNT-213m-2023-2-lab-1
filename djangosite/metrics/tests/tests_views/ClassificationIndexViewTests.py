from django.test import TestCase
from django.urls import reverse
from ...models import Measurement, Timestamps


class ClassificationIndexViewTests(TestCase):
    # def setUp(self):
    # Ваша підготовка даних, якщо потрібно, наприклад, створення об'єктів моделей

    def test_classification_index_view_with_params(self):
        # Створіть деякі тестові дані для передачі у запит
        test_data = {
            "temp": -7.17,
            "feels_like": -12.73,
            "temp_min": -8.56,
            "temp_max": -7.09,
            "pressure": 1030,
            "humidity": 53,
            "wind_speed": 3.6,
            "wind_deg": 310,
            "rain_1h": 0,
            "snow_1h": 0,
            "clouds_all": 20,
        }
        response = self.client.get(reverse('classification_index'), test_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertContains(
            response, 'RandomForestClassifier-based model with an accuracy of')

    def test_classification_index_view_without_params(self):
        url = reverse('classification_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(
            response, 'Error')
        self.assertContains(response, '<form')

    def test_classification_index_view_with_exception(self):
        wrong_data = {'measurement_id_1': '10.5', 'measurement_id_2': '20.0'}
        response = self.client.get(reverse('classification_index'), wrong_data)
        self.assertEqual(response.status_code, 500)
