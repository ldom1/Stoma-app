from django import forms
from django.apps import apps


class ControleTemperatureForm(forms.Form):

    '''collaborateurs = apps.get_model('collaborateurs', 'Collaborateur').objects.all()
    appareil = apps.get_model('appareil', 'Appareil').objects.all()

    choices_first_name_collaborateur = [[1, 'Choose...']] + [[y.first_name, y.first_name] for y in collaborateurs]
    choices_last_name_collaborateur = [[1, 'Choose...']] + [[y.last_name, y.last_name] for y in collaborateurs]
    choices_appareil = [[1, 'Choose...']] + [[y.name, y.name] for y in appareil]
    choices_appareil_location = [[1, 'Choose...']] + [[y.location, y.location] for y in appareil]
    choices_reception_period = [[1, 'Choose...'], ['matin', 'matin'], ['midi', 'midi'], ['apres-midi', 'apres-midi'], ['soir', 'soir'], ['nuit', 'nuit']]

    first_name_collaborateur = forms.ChoiceField(choices=choices_first_name_collaborateur, required=True)
    last_name_collaborateur = forms.ChoiceField(choices=choices_last_name_collaborateur, required=True)
    name_appareil = forms.ChoiceField(choices=choices_appareil, required=True)
    location_appareil = forms.ChoiceField(choices=choices_appareil_location, required=True)
    temperature = forms.FloatField(required=True)
    periode_releve = forms.ChoiceField(choices=choices_reception_period, required=True)
    description = forms.CharField(required=False)'''