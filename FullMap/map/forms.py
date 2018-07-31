from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['full_address', 'latitude', 'longitude', 'excluded_date', 'created_date', 'id']