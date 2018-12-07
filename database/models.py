# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.models import Country
from company.models import Company
from toolcomponents.models import ServerType


# Create your models here.
class DBType(models.Model):
	name=models.CharField(max_length=200,unique=True)
	
	def __unicode__(self):
		return u"%s" %(self.name)

	class Meta:
		verbose_name="DBType"
		verbose_name_plural="DBType"




class DBConfig(models.Model):
	config_name=models.CharField(max_length=100)
	host=models.CharField(max_length=100)
	port=models.IntegerField()
	username=models.CharField(max_length=100,blank=True,null=True)
	password=models.CharField(max_length=20)
	service_name=models.CharField(max_length=100, blank=True)
	SID=models.CharField(max_length=100, blank=True)
	DBName=models.CharField(max_length=100, blank=True)
	DBType=models.ForeignKey(DBType)
	companyId=models.ForeignKey(Company,null=True,blank=True)


	def __unicode__(self):
		return u"%s " %(self.config_name)

	class Meta:
		verbose_name="DBConfig"
		verbose_name_plural="DBConfig"

	
class DBCRUDType(models.Model):
	name=models.CharField(max_length=200)

	def __unicode__(self):
		return u"%s" %(self.name)

	class Meta:
		verbose_name="DBCRUDType"
		verbose_name_plural="DBCRUDType"




class ScriptExecution(models.Model):
	
	execution_name=models.CharField(max_length=200)
	companyId=models.ForeignKey(Company,blank=True,null=True)
	select_execution_operation=models.ForeignKey(DBCRUDType)
	sql_script=models.TextField(max_length=1000)
	#DBType=models.ForeignKey(DBType)
	
	function=models.CharField(max_length=200,blank=True,null=True)
	types=models.CharField(max_length=200,blank=True,null=True)
	script_dbtype=models.ForeignKey(DBType,blank=True,null=True)

	def __unicode__(self):
		return u" %s" %(self.execution_name)


	class Meta:
		verbose_name="ScriptExecution"
		verbose_name_plural="ScriptExecution"

	


class FTPExecution(models.Model):
	config_name=models.CharField(max_length=200)
	host=models.CharField(max_length=200)
	port=models.IntegerField()
	username=models.CharField(max_length=200)
	password=models.CharField(max_length=100)
	companyId=models.ForeignKey(Company,null=True,blank=True)
	targetdestination=models.TextField(max_length=500)
	
	# def __unicode__(self):
	# 	return u"%s %s %s %s %s" %(self.config_name,self.host,self.port,self.targetdestination)


	def __unicode__(self):
		return u"%s %s %s %s %s %s %s" %(self.config_name,self.host,self.port,self.username,self.password,self.companyId,self.targetdestination)


	class Meta:
		verbose_name="FTPExecution"
		verbose_name_plural="FTPExecution"



class AssignFTPUser(models.Model):
	username=models.CharField(max_length=200,blank=True,null=True)
	config_name=models.ForeignKey(FTPExecution,blank=True,null=True)

	class Meta:
		verbose_name="AssignFTPUser"
		verbose_name_plural="AssignFTPUser"


class AssignScriptUser(models.Model):
	username=models.CharField(max_length=200,blank=True,null=True)
	scriptexecute=models.ForeignKey(ScriptExecution,blank=True,null=True)
	# dbconfig_id=models.ForeignKey(DBConfig)
	def __unicode__(self):
		return u"%s %s " %(self.username,self.scriptexecute)

	class Meta:
		verbose_name="AssignScriptUser"
		verbose_name_plural="AssignScriptUser"



