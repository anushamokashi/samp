from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='company'


urlpatterns=[
	#url(r'^company_list/$', views.company_list),
	url(r'^execute/$', views.execute_details,name='execute_details'),
	url(r'^query/$',views.executeQuery,name='executeQuery'),
	url(r'^ftp/$',views.ftp,name='ftp'),
	url(r'^dbtype/$',views.dbtype,name='dbtype'),
	url(r'^dbtypeadd/$',views.dbtypeadd,name='dbtypeadd'),
	url(r'^dbtypeedit/(?P<dbid>\d+)/$',views.dbtypeedit,name='dbtypeedit'),
	url(r'^dbtypedel/(?P<id>\d+)/$',views.dbtypedel,name='dbtypedel'),
	url(r'^dbcrud/$',views.dbcrud,name='dbcrud'),
	url(r'^crudadd/$',views.crudadd,name='crudadd'),
	url(r'^cruddel/(?P<id>\d+)/$',views.cruddel,name='cruddel'),
	url(r'^crudedit/(?P<crud>\d+)/$',views.crudedit,name='crudedit'),
	url(r'^connectionTool/$',views.connectionTool,name='connectionTool'),
	url(r'^tooladd/$',views.tooladd,name='tooladd'),
	url(r'^deltool/(?P<id>\d+)/$',views.deltool,name='deltool'),
	url(r'^tooledit/(?P<tool>\d+)/$',views.tooledit,name='tooledit'),
	url(r'^servertype/$',views.servertype,name='servertype'),
	url(r'^serveradd/$',views.serveradd,name='serveradd'),
	url(r'^serveredit/(?P<servid>\d+)/$',views.serveredit,name='serveredit'),
	url(r'^servdel/(?P<id>\d+)/$',views.servdel,name='servdel'),
	url(r'^dbconfig/$',views.dbconfig,name='dbconfig'),
	url(r'^configadd/$',views.configadd,name='configadd'),
	url(r'^deldbconf/(?P<id>\d+)/$',views.deldbconf,name='deldbconf'),
	url(r'^dbconfigedit/(?P<config>\d+)/$',views.dbconfigedit,name='dbconfigedit'),
	url(r'^ftpadmin/$',views.ftpadmin,name='ftpadmin'),
	url(r'^ftpadd/$',views.ftpadd,name='ftpadd'),
	url(r'^delftp/(?P<id>\d+)/$',views.delftp,name='delftp'),
	url(r'^ftpedit/(?P<edit>\d+)/$',views.ftpedit,name='ftpedit'),
	url(r'^scriptexe/$',views.scriptexe,name='scriptexe'),
	url(r'^scriptadd/$',views.scriptadd,name='scriptadd'),
	url(r'^scriptedit/(?P<script>\d+)/$',views.scriptedit,name='scriptedit'),
	url(r'^delscript/(?P<id>\d+)/$',views.delscript,name='delscript'),

	url(r'^assignuserftp/$',views.assignUserftp,name='assignUserftp'),
	url(r'^assignuserscript/$',views.assignuserscript,name='assignuserscript'),

	url(r'^scriptassignexecute/$', views.scriptassignexecute,name='scriptassignexecute'),
	
	url(r'^scriptassignftpexecute/$', views.scriptassignftpexecute,name='scriptassignftpexecute'),

	url(r'^ftpcheckboxassign/$',views.ftpcheckboxassign,name='ftpcheckboxassign'),
	url(r'^scriptcheckboxassign/$',views.scriptcheckboxassign, name='scriptcheckboxassign'),

]
