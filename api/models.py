from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StatesUT(models.Model):
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100,primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'StatesUT'

class Cities(models.Model):
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100,primary_key=True)
    state = models.ForeignKey(StatesUT, models.DO_NOTHING)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Cities'

from auth_user.models import Huser
