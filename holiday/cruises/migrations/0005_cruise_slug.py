# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruises', '0004_remove_cruise_cruise_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruise',
            name='slug',
            field=models.URLField(default='', unique=True),
        ),
    ]
