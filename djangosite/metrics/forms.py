from django import forms
from .models import Timestamps, Location, Measurement

class TimestampEntryForm(forms.ModelForm):
    class Meta:
        model = Timestamps
        fields = ['measurement', 'value', 'location', 'date', 'time']
    
class LocationEntryForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'latitude', 'longitude']

class MeasurementEntryForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['name', 'description', 'unit']