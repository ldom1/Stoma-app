from django import forms
from django.apps import apps


class ControleReceptionForm(forms.Form):

    collaborateurs = apps.get_model('collaborateurs', 'Collaborateur').objects.all()
    fournisseurs = apps.get_model('fournisseur', 'Fournisseur').objects.all()

    choices_first_name_collaborateur = [[1, 'Choose...']] + [[y.first_name, y.first_name] for y in collaborateurs]
    choices_last_name_collaborateur = [[1, 'Choose...']] + [[y.last_name, y.last_name] for y in collaborateurs]
    choices_name_fournisseur = [[1, 'Choose...']] + [[y.name, y.name] for y in fournisseurs]
    choices_reception_period = [[1, 'Choose...'], ['matin', 'matin'], ['midi', 'midi'], ['apres-midi', 'apres-midi'], ['soir', 'soir'], ['nuit', 'nuit']]

    first_name_collaborateur = forms.ChoiceField(choices=choices_first_name_collaborateur, required=True)
    last_name_collaborateur = forms.ChoiceField(choices=choices_last_name_collaborateur, required=True)
    name_fournisseur = forms.ChoiceField(choices=choices_name_fournisseur, required=True)
    type_nourriture = forms.CharField(required=True)
    temperature = forms.FloatField(required=True)
    reception_period = forms.ChoiceField(choices=choices_reception_period, required=True)
    description = forms.CharField(required=False)