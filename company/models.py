# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from common.models import Country
# Create your models here.
class Company(models.Model):
	company_name=models.CharField(max_length=200)
	description=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	
	country=models.ForeignKey(Country)
	
	user = models.ForeignKey(User)


	def __unicode__(self):
		return u"%s %s %s" %(self.country,self.company_name,self.address)

	class Meta:
		verbose_name="Company"
		verbose_name_plural="Company"

	
class CompanyUserAssociation(models.Model):
	company_name=models.ForeignKey(Company)
	user=models.OneToOneField(User)

	class Meta:
		verbose_name="CompanyUserAssociation"
		verbose_name_plural="CompanyUserAssociation"