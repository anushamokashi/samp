# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_auto_20180727_1335'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='userscriptexecution',
        #     name='dbconfig_id',
        # ),
        # migrations.RemoveField(
        #     model_name='userscriptexecution',
        #     name='script_id',
        # ),
        # migrations.RemoveField(
        #     model_name='userscriptexecution',
        #     name='username_id',
        # ),
        migrations.DeleteModel(
            name='UserScriptExecution',
        ),
    ]
