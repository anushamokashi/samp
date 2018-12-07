# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib import messages

# Create your views here.



@csrf_exempt
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')




@csrf_exempt
def login(request):
	if request.method=='GET':
	    return render(request,"login.html")

	elif request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		print"hiiiiii"
		user=authenticate(username=username,password=password)

		failure_error = ''
		if user:
			if user.is_active:
				auth_login(request,user)
				
				messages.success(request, 'Your password was updated successfully!')
				return HttpResponseRedirect('/company_list/')
			else:
				failure_error = 'Your account is not yet verified,kindly wait for the E-Mail that you will receive from Dheep. Thank You.'
                return render_to_response('login.html',locals())

        else:
			messages.add_message(request, messages.INFO, 'Your username or password is invalid!....Check it once...')
			return HttpResponseRedirect('/login/')

    




