# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-24 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0024_auto_20180924_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scriptdbtype',
            options={'verbose_name': 'ScriptDbType', 'verbose_name_plural': 'ScriptDbType'},
        ),
        migrations.RemoveField(
            model_name='scriptexecution',
            name='script_dbtype',
        ),
    ]
