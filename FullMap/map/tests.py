import unittest
from django.urls import reverse
from django.test import Client
from .models import Location
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_location(**kwargs):
    defaults = {}
    defaults["full_address"] = "full_address"
    defaults["latitude"] = "latitude"
    defaults["longitude"] = "longitude"
    defaults["excluded_date"] = "excluded_date"
    defaults["created_date"] = "created_date"
    defaults["id"] = "id"
    defaults.update(**kwargs)
    return Location.objects.create(**defaults)


class LocationViewTest(unittest.TestCase):
    '''
    Tests for Location
    '''
    def setUp(self):
        self.client = Client()

    def test_list_location(self):
        url = reverse('map_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_location(self):
        url = reverse('map_location_create')
        data = {
            "full_address": "full_address",
            "latitude": "latitude",
            "longitude": "longitude",
            "excluded_date": "excluded_date",
            "created_date": "created_date",
            "id": "id",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_location(self):
        location = create_location()
        url = reverse('map_location_detail', args=[location.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        location = create_location()
        data = {
            "full_address": "full_address",
            "latitude": "latitude",
            "longitude": "longitude",
            "excluded_date": "excluded_date",
            "created_date": "created_date",
            "id": "id",
        }
        url = reverse('map_location_update', args=[location.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)