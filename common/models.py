# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
	country_name=models.CharField(max_length=200)
	country_code=models.IntegerField()

	def  __unicode__(self):
		return u"%s %s" %(self.country_name,self.country_code)

	class Meta:
		verbose_name="Country"
		verbose_name_plural="Country"

class State(models.Model):
	country_name=models.ForeignKey(Country)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return u"%s %s" %(self.name,self.country_name)

	class Meta:
		verbose_name="State"
		verbose_name_plural="States"

class City(models.Model):
	state_name=models.ForeignKey(State)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return u"%s %s" %(self.name,self.state_name)

	class Meta:
		verbose_name="City"
		verbose_name_plural="City"


	

