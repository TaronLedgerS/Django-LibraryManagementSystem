# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyLMS', '0006_auto_20171031_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='Book_id',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='Reader_id',
            new_name='Reader',
        ),
    ]
