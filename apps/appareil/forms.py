from django import forms
from django.apps import apps

class appareilForm(forms.Form):

	name = forms.CharField(required=True)
	location = forms.CharField(required=True)
	description = forms.CharField(required=False)