# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_auto_20180414_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbtype',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
