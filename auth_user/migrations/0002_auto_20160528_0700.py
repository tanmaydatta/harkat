# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='huser',
            old_name='city_id',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='huser',
            old_name='state_id',
            new_name='state',
        ),
    ]
