# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-19 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_scriptexecution_script_dbtype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScriptDbType',
        ),
    ]
