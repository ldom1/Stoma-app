from django import forms
from django.apps import apps

class collaborateurForm(forms.Form):

	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	description = forms.CharField(required=False)