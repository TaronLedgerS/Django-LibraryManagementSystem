# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyLMS', '0003_auto_20171031_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Book_ID'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Reader_ID'),
        ),
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Record_ID'),
        ),
    ]
