from . import models
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Location
        fields = (
            'pk', 
            'full_address', 
            'latitude', 
            'longitude', 
            'updated_date', 
            'excluded_date', 
            'created_date', 
            'id', 
        )