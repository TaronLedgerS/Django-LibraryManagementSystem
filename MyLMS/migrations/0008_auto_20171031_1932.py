# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyLMS', '0007_auto_20171031_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='Name',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]