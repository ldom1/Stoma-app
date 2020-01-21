from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.test.client import RequestFactory
from django.apps import apps
import numpy as np
import datetime

from .forms import *
from .models import *



class view_register_controle_reception(TemplateView):
	# Form to get data
    template_name = 'controle_reception/register_controle_reception.html'

    def get(self, request):
    	context = {}

    	form = ControleReceptionForm()
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}
    	form = ControleReceptionForm(request.POST)

    	if form.is_valid():

	    	first_name_collaborateur = form.cleaned_data['first_name_collaborateur']
	    	last_name_collaborateur = form.cleaned_data['last_name_collaborateur']
	    	name_fournisseur = form.cleaned_data['name_fournisseur']
	    	temperature = form.cleaned_data['temperature']
	    	type_nourriture = form.cleaned_data['type_nourriture']
	    	reception_period = form.cleaned_data['reception_period']
	    	description = form.cleaned_data['description']

	    	# Get the id
	    	'''controle_reception = ControleReception.objects.filter(user_username=request.user.get_username())
	    	id_collaborateur = apps.get_model('collaborateurs', 'Collaborateur').objects.filter(user_username=request.user.get_username(),
																							   first_name = first_name_collaborateur,
																							   last_name = last_name_collaborateur,)[0].id_collaborateur
	    	id_fournisseur = apps.get_model('fournisseur', 'Fournisseur').objects.filter(user_username=request.user.get_username(),
																					     name = name_fournisseur,)[0].id_fournisseur
	    	try:
	    		id_controle_reception = np.int(np.max([y.id_controle_reception for y in controle_reception]) + 1)
	    	except Exception:
	    		id_controle_reception = 1

	    	asset, created = ControleReception.objects.get_or_create(
						            	date = datetime.datetime.today(),
						            	id_controle_reception = id_controle_reception,
						            	id_collaborateur = id_collaborateur,
						            	id_fournisseur = id_fournisseur,
						            	first_name_collaborateur = first_name_collaborateur,
						            	last_name_collaborateur = last_name_collaborateur,
						            	name_fournisseur = name_fournisseur,
						            	temperature = temperature,
						            	periode_reception = reception_period,
						            	type_nourriture = type_nourriture,
		    							description = description,
		    							user_username = request.user.get_username())'''

    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)
    	

    		    

	    
