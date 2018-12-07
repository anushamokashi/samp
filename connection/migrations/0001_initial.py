# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0003_company_user'),
        ('toolcomponents', '0002_auto_20171027_0807'),
        ('database', '0004_auto_20171027_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigureConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_name', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('connection_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toolcomponents.ConnectionTool')),
                ('crud_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.DBCRUDType')),
                ('dbconfig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.DBConfig')),
                ('execution_script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.ScriptExecution')),
                ('server_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toolcomponents.ServerType')),
            ],
        ),
    ]
