# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-15 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyLMS', '0016_auto_20171115_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finestatistic',
            name='Begin_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finestatistic',
            name='End_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='finestatistic',
            name='Reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyLMS.Reader'),
        ),
    ]