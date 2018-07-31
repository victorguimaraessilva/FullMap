from django.contrib import admin
from django import forms
from .models import Location

class LocationAdminForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['full_address', 'latitude', 'longitude', 'updated_date', 'excluded_date', 'created_date', 'id']
    readonly_fields = ['full_address', 'latitude', 'longitude', 'updated_date', 'excluded_date', 'created_date', 'id']

admin.site.register(Location, LocationAdmin)