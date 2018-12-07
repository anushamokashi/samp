# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from connection.models import ConfigureConnection
Create your views here.
def connection(request):
	if request.method=='GET':
	    crud=ConfigureConnection.objects.all()
		# crud=ConfigureConnection.objects.filter(company.pk = int(compid))
		
	return render(request,"execute.html",{ "crud":crud })

	