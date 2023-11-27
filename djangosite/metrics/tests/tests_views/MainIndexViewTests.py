# tests.py
from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from ...models import Location, Measurement, Timestamps


class MainIndexViewTests(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='Test Location')
        self.measurement = Measurement.objects.create(name='Test Measurement')
        self.timestamp = Timestamps.objects.create(
            location=self.location, measurement=self.measurement, value="test", date=datetime.today().date(), time=datetime.today().time())

    def test_main_index_view(self):
        response = self.client.get(reverse('main_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "./main/index.html")

        self.assertContains(response, self.location.name)
        self.assertContains(response, self.measurement.name)
        self.assertContains(response, self.timestamp.date)
        self.assertContains(response, self.timestamp.value)

    def test_main_index_view_with_filter(self):
        response = self.client.get(reverse('main_index'), {
                                   'location': self.location.id, 'measurement': self.measurement.id, 'input_date': self.timestamp.date})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.location.name)
        self.assertContains(response, self.measurement.name)
