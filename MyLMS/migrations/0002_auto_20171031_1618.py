# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyLMS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='PWD',
            new_name='Password',
        ),
    ]