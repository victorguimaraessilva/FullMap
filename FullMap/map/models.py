from django.urls import reverse
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models


class Location(models.Model):

    id = models.PositiveIntegerField(primary_key=True)

    latitude = models.DecimalField(max_digits=8, decimal_places=3)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)

    full_address = models.CharField(max_length=255)

    created_date = models.DateTimeField()
    excluded_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk
