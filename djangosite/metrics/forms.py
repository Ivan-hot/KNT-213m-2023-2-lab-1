from django import forms
from .models import Timestamps, Location, Measurement


class TimestampEntryForm(forms.ModelForm):
    class Meta:
        model = Timestamps
        fields = ['measurement', 'value', 'location', 'date', 'time']
        widgets = {
            'measurement': forms.Select(attrs={"class": 'form-control'}),
            'value': forms.TextInput(attrs={"class": 'form-control'}),
            'location': forms.Select(attrs={"class": 'form-control'}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'time': forms.TimeInput(attrs={"class": "form-control"})
        }


class LocationEntryForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'latitude': forms.TextInput(attrs={"class": 'form-control'}),
            'longitude': forms.TextInput(attrs={"class": 'form-control'}),

        }


class MeasurementEntryForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['name', 'description', 'unit']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'description': forms.TextInput(attrs={"class": 'form-control'}),
            'unit': forms.TextInput(attrs={"class": 'form-control'}),

        }
