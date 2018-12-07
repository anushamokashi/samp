from __future__ import unicode_literals

from django.shortcuts import render
from .models import Company
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as auth_login
from connection.models import ConfigureConnection
from database.models import DBType , DBConfig,DBCRUDType,AssignScriptUser,AssignFTPUser
from database.models import ScriptExecution,FTPExecution
from toolcomponents.models import ConnectionTool,ServerType
import MySQLdb
import cx_Oracle                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
import re
import sys,connection
from django.core import serializers
import pysftp as sftp
from ftplib import FTP
import os
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage
import json
import mysql.connector 
import MySQLdb
from database.forms import DBConfigForm,FTPExecutionForm,ScriptExecutionForm,AssignScriptUserForm,AssignFTPUserForm
import sqlalchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.dialects import mysql
from django.conf import settings
from os import *
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def company_list(request):
		company_list = Company.objects.all()	
		return render(request,"company_list.html", {"company_list":company_list})

	
def execute_details(request):
	print request.method
	# crud=ConfigureConnection.objects.all()
	# script=ScriptExecution.objects.all()

	
	db_dbconf=DBConfig.objects.all()
	print db_dbconf,"..................dbconf.................."

	scrip_exec=ScriptExecution.objects.all()
	print scrip_exec,"...******>>>>>>>>>>.........."



	
	if request.method=='GET':
		print"enterscript....."
		username=request.GET['uname'] 
		# uname is from guacamole.js
		print username,"****"

		if username == "guacadmin":
			print"username",username
			# scriptobj=ScriptExecution.objects.all()
			# print scriptobj,"///"
			assign=AssignScriptUser.objects.filter(username=username)
		
			print assign,"assigned for guacadmin"

			

			return render(request,"execute.html", locals())

		else:
			assignedcount=AssignScriptUser.objects.filter(username=username).count()
			print assignedcount,"assignedcount...,count"

			if assignedcount == 0:
				scrtobj = ''
			else:
				assign=AssignScriptUser.objects.filter(username=username)
				print assign,"assignedscript....."
				slist=[]
				if assign:
					for s in assign:
						slist.append(s.scriptexecute_id)


				print slist,".............................................++++"

				# scriptobj=ScriptExecution.objects.filter(id__in=slist)
				# print scriptobj,"scriptobj...slist..........."

				

			return render(request,"execute.html",locals())

	
		

	elif request.is_ajax():

		id= request.POST.get('id')
		print "kkkkkkkkkkkkkkkkkkkkkk",id

		script=ScriptExecution.objects.get(id=id)


		db=DBConfig.objects.get(id=id)
		print "kkkk",db

	
		print "hhhhhh" ,db.DBType.name

		#if db.DBType.name=='mysql':
		print "hhhhhh" ,db.DBType.name


	return render(request,"execute.html",locals())


def executeQuery(request):
	print request.POST
	if request.method=="POST":
		dbid= request.POST.get('dbconf')
		print dbid,"dbid"
		sid = request.POST.get('value')
		print sid,"sid..."
		

		# db=ScriptExecution.objects.get(id=sid)
		
		db = ScriptExecution.objects.get(id = sid)
		print db

		db_config_id = db.id
		print db_config_id,"i will get radiobox id (scriptid)"

		db_config_type=DBConfig.objects.get(id=dbid)
		print db_config_type,"type of config..."

		db_type= db_config_type.DBType.name
		# db_config_id = assign.dbconfig_id.id
		# db_config_type=assign.dbconfig_id.DBType
		# print db_config_type,"1111111111111111111111111111111111"

		print db.sql_script,"////////////////////////////////"

		connection = createconnection(db_config_id,db_config_type,request)
		if db.select_execution_operation.name:

			if db.select_execution_operation.name=="insert":
				res =executeInsert(connection,db.sql_script)

			if db.select_execution_operation.name=="select":
				res = executeSelect(connection, db.sql_script)

			if db.select_execution_operation.name=="create":
				res =executeCreate(connection,db.sql_script)
				print res

			if db.select_execution_operation.name=="update":
				res=executeUpdate(connection,db.sql_script)

			if db.select_execution_operation.name =="delete":
				res=executeDelete(connection,db.sql_script)

			if db.select_execution_operation.name=="procedure":
				res=executeProcedure(connection,db.function,db.sql_script,db.types)

			if db.select_execution_operation.name=="function":
				res=executeFunction(connection,db.function,db.sql_script,db.types,db_type)

	return HttpResponse(res)

def createconnection(db,query,conf):
	
	print db,"............................"
	print query,".............query............"
	print conf,"..........................dd"

	connection=''
	db=DBConfig.objects.filter(id = db)
	list_of_db = DBType.objects.all()
	print list_of_db
	print db,"!@!#!#"

	# for i in list_of_db:
	# 	dbtype=i.name
	# 	print dbtype,"..PPPPPPPPPPPP......"
	# 	print query.DBType.name
	try:
		if query.DBType.name == 'oracle':
			print query.DBType.name,"oracle going to connect."
			print dbtype,"oracle connectinggg......"
			dsn_tns = cx_Oracle.makedsn(query.host, query.port, query.SID)
			connection = cx_Oracle.connect(query.username, query.password, dsn_tns)
			print "oracle connected"
			#return connection
		elif query.DBType.name == 'mysql':
			connection = MySQLdb.connect(query.host,query.username, query.password, query.DBName ,query.port)
			print "mysql connected...",connection

		return connection


	except Exception as e:
		print e

	# db_type = db.execution_name
	# print "......wt type of db...........",db_type

	# db_config = db.dbconfig
	# print '^^^^^^^^^^^^^^^^^^^',db_config

	# dbtype =db.dbconfig.DBType.name
	# print "......dbtype.....",dbtype 

 

def executeInsert(db,query):
	
	print "insert calling"

	cursor = db.cursor()
	
	try:
   
   		cursor.execute(query)

   		resp={}

		resp['data_type']='insert'
		resp['data_msg']='sucessfully inserted..'
		resp['data']=[]	


   	
   		print "inserted................."

    		
   		db.commit()
   		return json.dumps(resp)
   			
   		#insert= json.dumps(rows)
   		# print "aaaaaaa", insert

	except Exception as e:
  		db.rollback()
  		print "faileddddd"
  		resp={}
  		resp['data_type']='insert'
  		resp['data_msg']='not inserted'
  		resp['data']=[]
  		return json.dumps(resp)

  	finally:
  		cursor.close()
   		db.close()	

   	

def executeSelect(db,query):
	print db,"...tyope...."
	print 
	cursor = db.cursor()
   
	try:

		cursor.execute(query)
		print "sucessssssssssss select"

		rows=cursor.fetchall()

		columns = []
		for column in cursor.description:
			columns.append(column[0])

		data = {}
		data['columns'] = columns
		data['rows'] = rows


		resp={}

		resp['data_type']='select'
		resp['data_msg']='select working...'
		resp['data']=json.dumps(data)	

		select= json.dumps(resp)

		
		for row in rows:
			print row
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			
	except Exception as e:
		print e
		db.rollback()
		print "failed "
		resp={}

		resp['data_type']='select'
		resp['data_msg']=e
		resp['data']=[]

		select= json.dumps(resp)

	finally:
		cursor.close()
		db.close()
	return select  


def executeCreate(db,query):
		print db,"db...."
		print query,"query...."
		cursor = db.cursor()
		print query
		try:
			cursor.execute(query)
			
			resp={}

			resp['data_type']='create'
			resp['data_msg']='sucessfully created..'
			resp['data']=[]	

			print "sucessfully created................"

			db.commit()
			return json.dumps(resp)
			#return HttpResponse("sucessfully created..")

			

		except Exception as e:
			print e
			db.rollback()
			print "failed to create"
			resp={}
			resp['data_type']='create'
			resp['data_msg']='already created'
			resp['data']=[]	
			return json.dumps(resp)

		finally:	
			cursor.close()				
			db.close()


def executeUpdate(db,query):
	print db
	
	cursor = db.cursor()

	print "jjjjjjjjjjjjjjjjjjjjj"
	try:
		cursor.execute(query)
		# rows=cursor.fetchall()

		print "sucessfully updated..................."

		resp={}

		resp['data_type']='update'
		resp['data_msg']='sucessfully updated..'
		resp['data']=[]

		
		db.commit()
		return json.dumps(resp)

	except Exception as e:
		print e
		db.rollback()	
		print "failed to update"

		resp={}
		resp['data_type']='update'
		resp['data_msg']='not updated'
		resp['data']=[]

		
		return json.dumps(resp)

	finally:
		cursor.close()
		db.close()

def executeDelete(db,query):
		
	cursor = db.cursor()

	try:
		cursor.execute(query)
		# rows=cursor.fetchall()
		print "sucessfully deleted"
		resp={}
		resp['data_type']='delete'
		resp['data_msg']='successfully deleted'
		resp['data']=[]

		db.commit()
		return json.dumps(resp)
	except Exception as e:
		db.rollback()

		resp={}
		resp['data_type']='delete'
		resp['data_msg']='not deleted'
		resp['data']=[]
		return json.dumps(resp)
		print "failed............to delete"
		
	finally:
		cursor.close()
		db.close()

def executeFunction(db,function,query,types,db_type):
	print"function calling.."
	print db_type,",k,k,k,k,k"
	print "type of db for function",db_type
	
	# print db_config_type,"555"
	print db,"..........................db"

	print function,"...................func"
	print query,"....................query"
	print types,"...................types.."

	cursor=db.cursor()
	if db_type =="mysql":
		print "mysql function"

		try:
			print"....."
			print function
			print query,"this is quert"
			print types

			dtyp=""
			if types=="NUMBER":
				dtyp="NUMBER"

			elif types=="STRING":
				dtyp="STRING"

			print dtyp
			m = re.search(r"\((.*?)\)", query)
			print m,"11111"
			querystr = m.group(1)
			print querystr,"reexp"

			arylist =[]
			if "," in str(querystr) :
			
				arylist = querystr.split(",")
				print arylist,"123123"
			else :
			    arylist.append(querystr)
			

			res=cursor.callfunc(function,arylist)

			print "function"
			print res
			resp={}
			resp['data_type']='function'
			resp['data_msg']='function executed'
			resp['data']=[]

			return json.dumps(resp)

		except Exception as e:
			print e
		finally:
			cursor.close()
			db.close()
		

	elif db_type =="oracle":
		print db_type,"...dbtype..."
		print "oracle function............"
		try:
			print"........."
			print function
			print query
			print types

			dtyp =""
			if types=="NUMBER":
				dtyp= cursor.var(cx_Oracle.NUMBER)

			elif types=="STRING":
				dtyp=cursor.var(cx_Oracle.STRING)

			elif types=="CHAR":
				dtyp=cursor.var(cx_Oracle.CHAR)

			elif types=="DATE":
				dtyp=cursor.var(cx_Oracle.DATETIME)

			elif types=="TIMESTAMP":
				dtyp=cursor.var(cx_Oracle.TIMESTAMP)

			elif types=="CLOB":
				dtyp=cursor.var(cx_Oracle.CLOB)

			elif types=="BLOB":
				dtyp=cursor.var(cx_Oracle.BLOB)


			print dtyp
			m = re.search(r"\((.*?)\)", query)
			querystr = m.group(1)
			print "Array value",querystr
			arylist =[]
			if "," in str(querystr) :
			
				arylist = querystr.split(",")
			else :
			    arylist.append(querystr)
			# for a in arylist :
			# 	print a,"aaaaaaaa"

			print function

			res=cursor.callfunc(function,dtyp,arylist)

			print "function"
			print res
			resp={}
			resp['data_type']='function'
			resp['data_msg']='function executed'
			resp['data']=[]

			return json.dumps(resp)

		except Exception as e:
			print e
		finally:
			cursor.close()
			db.close()
	else:
		print "no database"




def executeProcedure(db,function,query,types):
	cursor = db.cursor()
	print function
	print query
	print types

	print"*********"
	try:
		
		dtyp =""
		if types=="NUMBER":
			dtyp= cursor.var(cx_Oracle.NUMBER)

		elif types=="STRING":
			dtyp=cursor.var(cx_Oracle.STRING)

		elif types=="CHAR":
			dtyp=cursor.var(cx_Oracle.DATETIME)

		elif types=="DATE":
			dtyp=cursor.var(cx_Oracle.DATETIME)

		elif types=="TIMESTAMP":
			dtyp=cursor.var(cx_Oracle.TIMESTAMP)

		elif types=="CLOB":
			dtyp=cursor.var(cx_Oracle.CLOB)

		elif types=="BLOB":
			dtyp=cursor.var(cx_Oracle.BLOB)
		
		print "procedure...calling"
		
		m = re.search(r"\((.*?)\)", query)
		querystr = m.group(1)
		print "Array value",querystr
		arylist =[]
		if "," in str(querystr) :
		
			arylist = querystr.split(",")
		else :
		    arylist.append(querystr)
		# for a in arylist :
		# 	print a,"aaaaaaaa"


		cursor.callproc(function, arylist)
		# print myvar.getvalue()

		
		resp={}
		resp['data_type']='procedure'
		resp['data_msg']='procedure executed'
		resp['data']=[]


		return json.dumps(resp)
		
	except Exception as e:
		print e

		
	finally:
		cursor.close()
		db.close()


def ftp(request):
	print"ftp.........."	

	if request.method=="GET":
		print"enterringgg"
		username=request.GET['uname']
		print username,"********"

		if username == "guacadmin":
			ftpobj=FTPExecution.objects.all()
			return render(request,"ftp.html",locals())
		else:

			assignedcount = AssignFTPUser.objects.filter(username=username).count()
			print assignedcount,"count."
			print  assignedcount == 0
        	
			if assignedcount == 0 :
				ftpobj = ''
				print ftpobj
			else :
				assignedftp = AssignFTPUser.objects.filter(username=username)
				print assignedftp,"assignedftp"
				slist = []

				if assignedftp :
					for s in assignedftp :
						slist.append(s.config_name_id)

        		print slist,"---------"
        		ftpobj=FTPExecution.objects.filter(id__in=slist)
        		print "ftpobj......",ftpobj
		
			return render(request,"ftp.html",locals())

	else :
   
		try:
			connectid=request.POST.get('id')
			print connectid
			print '-------=========---------'

			ftpobj=FTPExecution.objects.get(pk=connectid)

			
		except FTPExecution.DoesNotExist:
			print 'noooooo id'
			ftpobj=None
		
		print "Hi"	


		if ftpobj:
			cnopts = sftp.CnOpts()
			print "cnoptsss",cnopts
			cnopts.hostkeys = None

		try:
			with sftp.Connection(host=ftpobj.host,username=ftpobj.username,password=ftpobj.password,port=ftpobj.port,cnopts=cnopts) as srv:
				print("connected")
				
				file = request.FILES['FILE']
				print "mmmmmm",request.FILES
				fs = FileSystemStorage()
				filename = fs.save(file.name, file)
				print filename, "annnnnnnnnnnnnnn"
				print fs.location
				print fs.location+'/'+file.name, "jjjjjjjjjjjjjjj"
				uploaded_file_url = fs.url(filename)
				print '---------uploaded_file_url-----------'
				print uploaded_file_url
				print '/home/bcs/ftp.txt'
				print srv.pwd
				print '---------uploaded_fileupload_url-----------'
				with srv.cd(ftpobj.targetdestination):
					print '---------Inside direct-----------'
					print srv.pwd

					srv.put(fs.location+'/'+file.name,preserve_mtime=True)
					print "aaaaaa"
					os.remove(fs.location+'/'+file.name)
					print "aaaaaa"
						#result=srv.listdir()
				# return render(request,'ftp.html',locals())

		except Exception as e:
			print e
			print 'errorrrrrr'
	return HttpResponse('ok')		
   
	
def dbtype(request):
	print"dbtype...."
	if request.method=="POST":
		print request.POST
		dbtype=DBType.objects.create(name=request.POST.get('name'))
		print dbtype,"typesssssssss"

	db=DBType.objects.all()
	print db
	
	return render(request,"dbtype.html",locals())	

def dbtypeadd(request):
	return render(request,"dbtypeadd.html")	

def dbtypeedit(request,dbid):
	print"dbtypeediting...."
	print dbid
	dbname=DBType.objects.get(id = dbid)
	print dbname

	if request.method=="POST":
		db=DBType.objects.get(pk=dbid)
		print db
		print request.POST,"posting...."
		db.name = request.POST.get('name')
		print db.name,"nameuuu"
		dbname=DBType.objects.get(id = dbid)
		print dbname
		db.save()

		return HttpResponseRedirect('/dbtype/')
	else:
		return render(request,"dbtypeedit.html",locals())

def dbtypedel(request,id):
	print"deleting...."
	print id
	dbdel=DBType.objects.get(pk=id)
	print dbdel,"............."
	dbdel.delete()

	return HttpResponseRedirect('/dbtype/')


def dbcrud(request):
	print"crudcreate.."
	if request.method=="POST":
		print request.POST
		crudtype=DBCRUDType.objects.create(name=request.POST.get('name'))

	crud=DBCRUDType.objects.all()
	print "cruding..",crud

	return render(request,"dbcrud.html",locals())

def crudadd(request):
	print"adding..."

	return render(request,"crudadd.html")

def cruddel(request,id):
	print"deleting..."
	cruddel=DBCRUDType.objects.get(pk=id)
	cruddel.delete()

	return HttpResponseRedirect('/dbcrud/')

def crudedit(request,crud):
	print"editing..."
	print crud
	crd=DBCRUDType.objects.get(pk=crud)
	print crd,".........."
	if request.method=="POST":
		crud=DBCRUDType.objects.get(pk=crud)
		print "cruding....",crud
		crud.name=request.POST.get('name')
		print "name...",crud.name
		crud.save()
		return HttpResponseRedirect('/dbcrud/')
	else:

		return render(request,"dbcrudedit.html",locals())


def dbconfig(request):
	print"dbconfig..."

	form_class = DBConfigForm
   
	form = form_class(request.POST or None)
	if request.method == "POST":
		print request.POST
		form = DBConfigForm(request.POST)
		if form.is_valid():
			print"valid...."
			new = form.save(commit=False)
			new.DBType_id = request.POST['DBType']
			# new.companyId_id = request.POST['companyId']
			new.save()
		else:
			print form.errors

		dbconfigdetails = DBConfig.objects.all()
		return render(request,"dbconfig.html",locals())
	else:
		dbconfigdetails = DBConfig.objects.all()
		print dbconfigdetails
		return render(request,"dbconfig.html",locals())

def deldbconf(request,id):
	print"deleting...."
	delconf=DBConfig.objects.get(pk=id)
	delconf.delete()

	return HttpResponseRedirect('/dbconfig/')

def configadd(request):
	print "adding...."
	db=DBType.objects.all()
	company_list=Company.objects.all()

	return render(request,"configadd.html",locals())

def dbconfigedit(request,config):
	print"editing..."
	confedit=DBConfig.objects.get(pk=config)
	print confedit,"edit..."
	db=DBType.objects.all()
	company_list=Company.objects.all()

	if request.method=="POST":
		print request.POST
		form=DBConfigForm(request.POST,instance=confedit)
		dbconfigdetails = DBConfig.objects.all()
		if form.is_valid():
			confupdate=form.save(commit=False)
			confupdate.DBType_id = request.POST['DBType']
			# confupdate.companyId_id = request.POST['companyId']
			confupdate.save()
			return HttpResponseRedirect('/dbconfig/')

		else:
			print form.errors

		
		return render(request,"dbconfig.html",locals())
	else:
		form = DBConfigForm(instance=confedit)

		return render(request,"dbconfigedit.html",locals())


def connectionTool(request):
	print"connectt,...."
	if request.method=="POST":
		print request.POST
		connect=ConnectionTool.objects.create(ToolName=request.POST.get('name'))
		print connect,"..................."

	connection=ConnectionTool.objects.all()
	print connection,"^^^^^^^^^^^^^^^6"
	return render(request,"connecttool.html",locals())

def tooladd(request):
	print"adding..."

	return render(request,"tooladd.html",locals())


def deltool(request,id):
	print"deletin..."
	deltool=ConnectionTool.objects.get(pk=id)
	deltool.delete()
	return HttpResponseRedirect('/connectionTool/')

def tooledit(request,tool):
	print"tooledit..."
	print tool
	tool_edit=ConnectionTool.objects.get(pk=tool)
	print tool_edit,"......."
	if request.method=="POST":
		print request.POST

		tool=ConnectionTool.objects.get(pk=tool)
		print tool,",kldjsoflo"
		tool.ToolName=request.POST.get('ToolName')
		print tool.ToolName,"llllllllllll"
		tool.save()

		return HttpResponseRedirect('/connectionTool/')
	else:
		return render(request,"tooledit.html",locals())


def servertype(request):
	print"types...."
	if request.method=="POST":
		print request.POST
		servertype=ServerType.objects.create(ServerName=request.POST.get('name'))
		print servertype,",......create..........."

	server=ServerType.objects.all()
	print server,"server..."

	return render(request,"servertype.html",locals())

def serveradd(request):
	print"adding...."

	return render(request,"serveradd.html",locals())

def serveredit(request,servid):
	print"editing..."
	server_edit=ServerType.objects.get(pk=servid)
	print server_edit,"......."
	if request.method=="POST":
		print request.POST

		servedit=ServerType.objects.get(pk=servid)
		print "servedit.....",servedit

		servedit.ServerName=request.POST.get('ServerName')
		print"serveredit%%%%%%%%%%",servedit.ServerName

		servedit.save()

		return HttpResponseRedirect('/servertype/')
	else:
		return render(request,"serveredit.html",locals())

def servdel(request,id):

	servdel=ServerType.objects.get(pk=id)
	servdel.delete()

	return HttpResponseRedirect('/servertype/')

def ftpadmin(request):
	print"hiiiftp"

	if request.method=="POST":
		print request.POST
		form=FTPExecutionForm(request.POST)

		if form.is_valid():
			print"ftpvalid"
			ftpadmin=form.save(commit=False)
			# ftpadmin.companyId_id = request.POST['companyId']
			ftpadmin.save()
		else:
			print form.errors

		ftp=FTPExecution.objects.all()
		return render(request,"ftpadmin.html",locals())
	else:	
		ftp=FTPExecution.objects.all()
		return render(request,"ftpadmin.html",locals())

def ftpadd(request):
	print"add......"
	company_list=Company.objects.all()
	ftp=FTPExecution.objects.all()

	return render(request,"ftpadd.html",locals())

def delftp(request,id):
	print"deleting..."
	ftpdel=FTPExecution.objects.get(pk=id)
	ftpdel.delete()

	return HttpResponseRedirect('/ftpadmin/')

def ftpedit(request,edit):
	print"ftpedit..."
	ftpedit=FTPExecution.objects.get(pk=edit)
	print ftpedit,".........."
	company_list=Company.objects.all()

	if request.method=="POST":
		print request.POST
		form=FTPExecutionForm(request.POST,instance=ftpedit)
		ftp=FTPExecution.objects.all()
		if form.is_valid():
			ftpupdate=form.save(commit=False)
			# ftpupdate.companyId_id = request.POST['companyId']
			ftpupdate.save()
			return HttpResponseRedirect('/ftpadmin/')
		else:
			print form.errors
		return render(request,"ftpedit.html",locals())

	else:
		form=FTPExecutionForm(instance=ftpedit)
		return render(request,"ftpedit.html",locals())


def scriptexe(request):
	print"script...."

	if request.method=="POST":
		print request.POST,"posting......"
		form=ScriptExecutionForm(request.POST)
		scr_exe=ScriptExecution.objects.all()	
		print scr_exe,"....................."

		if form.is_valid():
			print"scriptvalid....."
			scriptform=form.save(commit=False)
			# scriptform.companyId_id=request.POST['companyId']
			scriptform.select_execution_operation_id=request.POST['select_execution_operation']
			scriptform.script_dbtype_id = request.POST['script_dbtype']
			
			scriptform.save()
		else:
			print form.errors
		scr_exe=ScriptExecution.objects.all()	
		return render(request,"scriptexecution.html",locals())
	else:
		scr_exe=ScriptExecution.objects.all()	
		return render(request,"scriptexecution.html",locals())



def scriptadd(request):
	print"adding..."
	company_list=Company.objects.all()
	crud=DBCRUDType.objects.all()
	scr_exe=ScriptExecution.objects.all()	
	scrp_type=DBType.objects.all()
	
	return render(request,"scriptadd.html",locals())

def scriptedit(request,script):
	print"scriptedit....."

	company_list=Company.objects.all()
	crud=DBCRUDType.objects.all()
	server=ServerType.objects.all()
	dbconfigdetails = DBConfig.objects.all()
	scrp_type= DBType.objects.all()
	scr_edit=ScriptExecution.objects.get(pk=script)
	print scr_edit,"llklklk"
	if request.method=="POST":
		print request.POST
		request.POST['select_execution_operation']
		form=ScriptExecutionForm(request.POST,instance=scr_edit)
		if form.is_valid():
			scr_upd=form.save(commit=False)
		
			scr_upd.select_execution_operation_id=request.POST['select_execution_operation']
			scr_upd.script_dbtype_id = request.POST['script_dbtype']
			scr_upd.save()
			return HttpResponseRedirect('/scriptexe/')
		else:
			print form.errors

		return render(request,"scriptedit.html",locals())
	else:
		form=ScriptExecutionForm(instance=scr_edit)
		return render(request,"scriptedit.html",locals())




def delscript(request,id):
	print "deleting......"
	delscript=ScriptExecution.objects.get(pk=id)
	print delscript
	delscript.delete()
	return HttpResponseRedirect('/scriptexe/')



def assignUserftp(request):
	print"usertool...."
	# ftp=AssignFTPUser.objects.all()
	# print ftp


	ftp=FTPExecution.objects.all()
	print ftp

	


	dbHost = settings.DATABASES['default']['HOST']
	dbUsername = settings.DATABASES['default']['USER']
	dbPassword = settings.DATABASES['default']['PASSWORD']
	dbName = settings.DATABASES['default']['NAME']
	dbPort = settings.DATABASES['default']['PORT']

	# database_url = "%s:%s@%s:%s/%s" % ('dbUsername', 'dbPassword', 'dbHost', dbPort, 'dbName')
	# server = create_engine("mysql://"+ database_url, echo=True)
	print dbHost,"HGGKJGJK"
	db = MySQLdb.connect('192.168.124.172','root','MySQLRootPass','guacdb',3306)
	# db=MySQLdb.connect('dbUsername', 'dbPassword', 'dbHost', dbPort, 'dbName')
	# db=MySQLdb.connect(host=dbHost,user=dbUsername,passwd=dbPassword,db=dbName,port=dbPort)
	print "db....",db
	cursor = db.cursor()

	cursor.execute("select username from  guacamole_user")


	data = cursor.fetchall()
	print data,"[[[[[[[[[[]]]]]]]]]]]]]]"

	list=[]
	for i in data:
		print i[0],"iiiiiiiiiiiiiii"
		list.append(i[0])

	print list



	db.close()


	return render(request,"assignuserftp.html",locals())

def assignuserscript(request):
	print"usertoolscript...."
	
	script=ScriptExecution.objects.all()
	print script

	scriptcount =ScriptExecution.objects.count()
	print scriptcount

	dbconfigdetails = DBConfig.objects.all()
	scr_ass=AssignScriptUser.objects.all()
	print scr_ass,"11111111111111111111111111111111111111111"
	
	dbHost = settings.DATABASES['default']['HOST']
	dbUsername = settings.DATABASES['default']['USER']
	dbPassword = settings.DATABASES['default']['PASSWORD']
	dbName = settings.DATABASES['default']['NAME']
	dbPort = settings.DATABASES['default']['PORT']

	# database_url = "%s:%s@%s:%s/%s" % ('dbUsername', 'dbPassword', 'dbHost', dbPort, 'dbName')
	# server = create_engine("mysql://"+ database_url, echo=True)
	print dbHost,"HGGKJGJK"
	db = MySQLdb.connect('192.168.124.172','root','MySQLRootPass','guacdb',3306)
	# db=MySQLdb.connect('dbUsername', 'dbPassword', 'dbHost', dbPort, 'dbName')
	# db=MySQLdb.connect(host=dbHost,user=dbUsername,passwd=dbPassword,db=dbName,port=dbPort)
	print "db....",db
	cursor = db.cursor()

	cursor.execute("select username from  guacamole_user")


	data = cursor.fetchall()
	print data,"[[[[[[[[[[]]]]]]]]]]]]]]"

	list=[]
	for i in data:
		print i[0],"iiiiiiiiiiiiiii"
		list.append(i[0])

	print list



	db.close()


	return render(request,"assignuserscript.html",locals())


def scriptassignexecute(request):
	print"scriptexecute"
	dbconfigdetails = DBConfig.objects.all()
	
	if request.method=="POST":
		print request.POST
		username = request.POST['username']
		chkval = request.POST['chkval']
		# dbconf = request.POST['dbconf']


		print username
		print chkval

		form=AssignScriptUserForm(request.POST)

		if form.is_valid():
			print"valid"
			AssignScriptUser.objects.filter(username=username).delete()

			chksplit = chkval.split(',')
			# dbconfsplit = dbconf.split(',')
			for chk in chksplit:
				if chk :
					print chk
					scr_usr=AssignScriptUser()
					scr_usr.scriptexecute_id = int(chk)
					scr_usr.username = username
					# scr_usr.dbconfig_id_id=dbconfsplit[i]
					# print dbconfsplit[i],"qwerty"
					scr_usr.save()

			
			
		else:
			print form.errors
			return render(request,"assignuserscript.html", locals())


	return render(request,"assignuserscript.html", locals())



def scriptassignftpexecute(request):

	print "ftpscript......"

	

	if request.method=="POST":
		username=request.POST['username']

		chkval = request.POST['chkval']
		# display_type = request.POST.get("check", None)
		print username
		print chkval

		form=AssignFTPUserForm(request.POST)

		if form.is_valid():
			print"valid"
			# if ('check').checked  in request.POST:
			assign=AssignFTPUser.objects.filter(username=username).delete()
			print assign
			# display=request.POST["check"]
			# print display,"displayinggggg"

			chksplit = chkval.split(',')
			print chksplit,"split...."
			for chk in chksplit :
				if chk :
					print chk,"&&&&&&&&"
					scr_usr=AssignFTPUser()
					print scr_usr
					scr_usr.config_name_id = int(chk)
					scr_usr.username = username
						# request.POST.getlist('check')
					scr_usr.save()

			return HttpResponse("success")
			
			
		else:
			print form.errors

			return HttpResponse("success")
			# return render(request,"assignuserftp.html", locals())



	return render(request,"assignuserftp.html",locals())


def ftpcheckboxassign(request):
	
	print "ajax calling...."

	
	
	if request.is_ajax():
		username = request.POST['username'].strip()
		ftpuser=AssignFTPUser.objects.filter(username=username).count()
        data = {}
        if ftpuser == 0 :
        	data['count'] = ftpuser
        else:
        	data['count'] = ftpuser
        	chk = ''
        	ftpchk = AssignFTPUser.objects.filter(username=username)
        	print ftpchk,"..........ftpchk........."
        	for f in ftpchk :
        		chk = chk + str(f.config_name_id) + ","
        	print chk
        	data['checked'] = chk

        return HttpResponse(json.dumps(data))


	
def scriptcheckboxassign(request):

	print "script ajax..." 
	# scr_exe=ScriptExecution.objects.all()	

	if request.is_ajax():
		username=request.POST['username'].strip()
		scriptchk=AssignScriptUser.objects.filter(username=username)
		print username,"$$$$$$$$$$$$$$$$$$$$$"
		scriptuser=scriptchk.count()
		print scriptuser,'kkkkk'
		data = {}

		if scriptuser == 0:
			data['count'] =scriptuser
		else:
			data['count'] = scriptuser
			chk = ''
			scriptchk=AssignScriptUser.objects.filter(username=username)
			print scriptchk,"2222"

			checkedlist = []

			for s in scriptchk:
				datadict = {}
				datadict['id'] = s.id
				datadict['username'] = s.username
				datadict['scriptname_id'] = s.scriptexecute_id
				datadict['scriptname'] = s.scriptexecute.execution_name
				# datadict['dbconfig_id'] = s.dbconfig_id_id
				# datadict['dbconfig'] = s.dbconfig_id.config_name
				checkedlist.append(datadict)
			
			data['checked'] = checkedlist

		return HttpResponse(json.dumps(data))
