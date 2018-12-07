# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ConnectionTool(models.Model):
	ToolName=models.CharField(max_length=200)

	def __str__(self):
		return self.ToolName

	class Meta:
		verbose_name="ConnectionTool"
		verbose_name_plural="ConnectionTool"

class ServerType(models.Model):
	ServerName=models.CharField(max_length=200)

	def __str__(self):
		return self.ServerName

	
	class Meta:
		verbose_name="ServerType"
		verbose_name_plural="ServerType"