from django import forms
from django.apps import apps

class appareilForm(forms.Form):

	'''piece = apps.get_model('piece', 'Piece').objects.all()
	choices_piece = [[1, 'Choose...']] + [[y.name_piece, y.name_piece] for y in piece]

	name = forms.CharField(required=True)
	location = forms.ChoiceField(choices=choices_piece, required=True)
	description = forms.CharField(required=False)'''