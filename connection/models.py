# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from company.models import Company
from toolcomponents.models import ConnectionTool
from toolcomponents.models import ServerType
from database.models import DBConfig
from database.models import DBCRUDType
from database.models import ScriptExecution

# Create your models here.
class ConfigureConnection(models.Model):
	connection_name=models.CharField(max_length=200)
	company=models.ForeignKey(Company)
	server_name=models.ForeignKey(ServerType)
	dbconfig=models.ForeignKey(DBConfig)
	crud_type=models.ForeignKey(DBCRUDType)
	execution_script=models.TextField(max_length=1000)

	


	def __unicode__(self):
		return u"%s %s %s %s %s %s" %(self.connection_name ,self.company, self.server_name,self.dbconfig,self.crud_type,self.execution_script)