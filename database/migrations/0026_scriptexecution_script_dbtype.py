# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-24 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0025_auto_20180924_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='scriptexecution',
            name='script_dbtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DBType'),
        ),
    ]
