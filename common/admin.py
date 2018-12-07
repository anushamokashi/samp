# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Country,State,City

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
	list_filter=('country_name','country_code',)
	search_fields=('country_name','country_code',)

admin.site.register(Country,CountryAdmin)


class StateAdmin(admin.ModelAdmin):
	list_filter=('name','country_name__country_name',)
	search_fields=('name','country_name__country_name',)

admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
	list_filter=('name','state_name__name',)
	search_fields=('name','state_name__name',)

admin.site.register(City,CityAdmin)