from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from api.models import Cities, StatesUT
# Create your models here.


class Huser(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=30)
    city = models.ForeignKey(Cities, models.DO_NOTHING,null=True)
    state = models.ForeignKey(StatesUT, models.DO_NOTHING)
    email = models.EmailField(max_length=254,unique=True)
    fb_id = models.BigIntegerField(default=-1)
    g_id = models.BigIntegerField(default=-1)


    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'User'

