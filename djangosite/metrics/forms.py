from django import forms
from .models import Timestamps

class TimestampEntryForm(forms.ModelForm):
    class Meta:
        model = Timestamps
        fields = ['measurement', 'value', 'location', 'date', 'time']
    