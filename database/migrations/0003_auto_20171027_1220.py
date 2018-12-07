# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20171027_0807'),
        ('database', '0002_dbcrudtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptExecution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution_name', models.CharField(max_length=200)),
                ('sql_script', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dbconfig',
            options={'verbose_name': 'DBConfig', 'verbose_name_plural': 'DBConfig'},
        ),
        migrations.AlterModelOptions(
            name='dbcrudtype',
            options={'verbose_name': 'DBCRUDType', 'verbose_name_plural': 'DBCRUDType'},
        ),
        migrations.AlterModelOptions(
            name='dbtype',
            options={'verbose_name': 'DBType', 'verbose_name_plural': 'DBType'},
        ),
        migrations.AddField(
            model_name='dbconfig',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Country'),
        ),
        migrations.AddField(
            model_name='dbconfig',
            name='config_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scriptexecution',
            name='DBType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.DBConfig'),
        ),
        migrations.AddField(
            model_name='scriptexecution',
            name='select_execution_operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.DBCRUDType'),
        ),
    ]
