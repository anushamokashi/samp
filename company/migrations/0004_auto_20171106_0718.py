# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='city',
        ),
        migrations.RemoveField(
            model_name='company',
            name='state',
        ),
    ]
