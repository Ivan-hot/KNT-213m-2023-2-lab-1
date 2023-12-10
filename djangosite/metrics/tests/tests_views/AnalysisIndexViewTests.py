from django.test import TestCase
from django.urls import reverse
from datetime import datetime, timedelta
from ...models import Location, Measurement, Timestamps


class AnalysisIndexViewTests(TestCase):

    def setUp(self):
        self.location = Location.objects.create(name='Test Location')
        self.measurement = Measurement.objects.create(
            name='Test Measurement', unit='category')
        self.timestamp = Timestamps.objects.create(
            location=self.location, measurement=self.measurement, value="test", date=datetime.today().date(), time=datetime.today().time())

    def test_analysis_index_view(self):
        response = self.client.get(reverse('analysis_index'), {
            'location': self.location.id,
            'measurement': self.measurement.id,
            'date_from': self.timestamp.date - timedelta(days=10),
            'date_to': self.timestamp.date + timedelta(days=10),
        })

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.location.name)
        self.assertContains(response, self.measurement.name)

        if self.measurement.id and self.location.id:
            self.assertGreater(len(response.context['images']), 0)
        else:
            self.assertEqual(len(response.context['images']), 0)
