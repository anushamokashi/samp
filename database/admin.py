# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import DBType,DBConfig,DBCRUDType,ScriptExecution,FTPExecution,AssignScriptUser
# Register your models here.
class DBTypeAdmin(admin.ModelAdmin):
	list_filter=('name',)
	search_fields=('name',)
admin.site.register(DBType,DBTypeAdmin)

class DBConfigAdmin(admin.ModelAdmin):
	list_filter=('host','port','DBName',)
	search_fields=('host','port','DBName',)
admin.site.register(DBConfig,DBConfigAdmin)


class DBCRUDTypeAdmin(admin.ModelAdmin):
	list_filter=('name',)
	search_fields=('name',)
admin.site.register(DBCRUDType,DBCRUDTypeAdmin)

admin.site.register(ScriptExecution)
admin.site.register(FTPExecution)
admin.site.register(AssignScriptUser)
