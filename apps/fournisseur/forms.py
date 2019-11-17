from django import forms
from django.apps import apps

class fournisseurForm(forms.Form):

	name = forms.CharField(required=True)
	description = forms.CharField(required=True)
	adress = forms.CharField(required=False)
	zip_code = forms.IntegerField(required=False)
	siren = forms.IntegerField(required=False)