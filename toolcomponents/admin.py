# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ConnectionTool,ServerType
# Register your models here.


class ConnectionToolAdmin(admin.ModelAdmin):
	list_filter=('ToolName',)
	search_fields=('ToolName',)
admin.site.register(ConnectionTool,ConnectionToolAdmin)


class ServerTypeAdmin(admin.ModelAdmin):
	list_filter=('ServerName',)
	search_fields=('ServerName',)
admin.site.register(ServerType,ServerTypeAdmin)



