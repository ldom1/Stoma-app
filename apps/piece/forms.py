from django import forms
from django.apps import apps

class pieceForm(forms.Form):

	name_piece = forms.CharField(required=True)
	description = forms.CharField(required=False)