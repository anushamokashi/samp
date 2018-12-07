 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Company,CompanyUserAssociation
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
	list_display = (
		'company_name',
		'description',
		'address',
		'country',
		
	)
	list_filter=('company_name','description','address','country')
	search_fields=('company_name','description','address','country')
admin.site.register(Company,CompanyAdmin)

class CompanyUserAssociationAdmin(admin.ModelAdmin):
	list_filter=('company_name__company_name',)
	search_fields=('company_name__company_name',)
admin.site.register(CompanyUserAssociation,CompanyUserAssociationAdmin)