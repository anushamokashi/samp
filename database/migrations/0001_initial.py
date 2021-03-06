# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('service_name', models.CharField(max_length=100)),
                ('SID', models.CharField(max_length=100)),
                ('DBName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DBType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='dbconfig',
            name='DBType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.DBType'),
        ),
    ]
