from django.apps import apps
from django import forms
from django.forms import ModelForm, DateInput
from plan_nettoyage.models import PlanNettoyage

class PlanNettoyageForm(ModelForm):

  class Meta:

    model = PlanNettoyage
    # datetime-local is a HTML5 input type, format to make date time show on fields

    piece = apps.get_model('piece', 'Piece').objects.all()
    collaborateurs = apps.get_model('collaborateurs', 'Collaborateur').objects.all()
    '''piece = apps.get_model('piece', 'Piece').objects.all()

    choices_first_name_collaborateur = [[1, 'Choose...']] + [[y.first_name, y.first_name] for y in collaborateurs]
    choices_last_name_collaborateur = [[1, 'Choose...']] + [[y.last_name, y.last_name] for y in collaborateurs]
    choices_piece = [[1, 'Choose...']] + [[y.name_piece, y.name_piece] for y in piece]
    
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'first_name_collaborateur': forms.Select(choices=choices_first_name_collaborateur,  attrs={'class': 'form-control'}),
      'last_name_collaborateur': forms.Select(choices=choices_last_name_collaborateur, attrs={'class': 'form-control'}),
      'piece': forms.Select(choices=choices_piece, attrs={'class': 'form-control'}),
    }

    fields = ('title', 'start_time', 'end_time', 'description', 'first_name_collaborateur', 'last_name_collaborateur', 'piece')

  def __init__(self, *args, **kwargs):

    super(PlanNettoyageForm, self).__init__(*args, **kwargs)
    
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)'''