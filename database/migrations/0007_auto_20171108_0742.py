# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20171106_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scriptexecution',
            name='DBType',
        ),
        migrations.AddField(
            model_name='scriptexecution',
            name='dbconfig',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.DBConfig'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dbconfig',
            name='companyId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
        ),
    ]
