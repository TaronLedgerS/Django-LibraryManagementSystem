# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyLMS', '0005_auto_20171031_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]