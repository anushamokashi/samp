# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-24 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0022_auto_20180918_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptDbType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scriptdbtype', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='scriptexecution',
            name='script_dbtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.ScriptDbType'),
        ),
    ]
