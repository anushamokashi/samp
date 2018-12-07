from django.forms import ModelForm

from django.forms import formset_factory
from django import forms
from .models import DBConfig,FTPExecution,ScriptExecution,AssignFTPUser,AssignScriptUser,AssignFTPUser

class DBConfigForm(ModelForm):
    class Meta:
        model = DBConfig
        fields='__all__'
        exclude=['DBType','companyId']

class FTPExecutionForm(ModelForm):
	class Meta:
		model =FTPExecution
		fields='__all__'
		exclude=['companyId']


class ScriptExecutionForm(ModelForm):
	class Meta:
		model=ScriptExecution
		fields='__all__'
		exclude=['companyId','select_execution_operation','script_dbtype']



class AssignScriptUserForm(ModelForm):
	class Meta:
		model=AssignScriptUser
		fields='__all__'
		exclude=['scriptexecute']


class AssignFTPUserForm(ModelForm):
	class Meta:
		model=AssignFTPUser
		fields='__all__'
		exclude=['config_name']

