from django.test import TestCase
from ...forms import LocationEntryForm

class FormTestCase(TestCase):
    def test_form_fields(self):
        # Check that the form contains the expected fields
        form = LocationEntryForm()
        expected_fields = ['name', 'latitude', 'longitude']
        self.assertCountEqual(form.fields.keys(), expected_fields)

    def test_form_valid_data(self):
        # Check that the form is considered valid with correct data
        form_data = {
            'name': 'Test Location',
            'latitude': '40.7128',
            'longitude': '-74.0060'
        }
        form = LocationEntryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_valid_data_blank_name(self):
        # Check that the form is considered invalid when name is blank
        form_data = {
            'name': '',
            'latitude': '40.7128',
            'longitude': '-74.0060'
        }
        form = LocationEntryForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_valid_data_blank_longitude(self):
        # Check that the form is considered invalid when longitude is blank
        form_data = {
            'name': 'Test Location',
            'latitude': '40.7128',
            'longitude': ''
        }
        form = LocationEntryForm(data=form_data)
        self.assertFalse(form.is_valid())


# python manage.py test metrics.tests.tests_models.ModelTestCase