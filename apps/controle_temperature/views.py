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



class view_register_controle_temperature(TemplateView):
	# Form to get data
    template_name = 'controle_temperature/register_controle_temperature.html'

    def get(self, request):
    	context = {}

    	form = ControleTemperatureForm()
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}
    	form = ControleTemperatureForm(request.POST)

    	if form.is_valid():

	    	first_name_collaborateur = form.cleaned_data['first_name_collaborateur']
	    	last_name_collaborateur = form.cleaned_data['last_name_collaborateur']
	    	name_appareil = form.cleaned_data['name_appareil']
	    	location_appareil = form.cleaned_data['location_appareil']
	    	temperature = form.cleaned_data['temperature']
	    	periode_releve = form.cleaned_data['periode_releve']
	    	description = form.cleaned_data['description']

	    	# Get the id
	    	controle_temperature = ControleTemperature.objects.filter(user_username=request.user.get_username())
	    	id_collaborateur = apps.get_model('collaborateurs', 'Collaborateur').objects.filter(user_username=request.user.get_username(),
																							   first_name = first_name_collaborateur,
																							   last_name = last_name_collaborateur,)[0].id_collaborateur
	    	id_appareil = apps.get_model('appareil', 'Appareil').objects.filter(user_username=request.user.get_username(),
																			    name = name_appareil,
																			    location=location_appareil)[0].id_appareil
	    	try:
	    		id_controle_temperature = np.int(np.max([y.id_controle_temperature for y in controle_temperature]) + 1)
	    	except Exception:
	    		id_controle_temperature = 1

	    	asset, created = ControleTemperature.objects.get_or_create(
						            	date = datetime.datetime.today(),
						            	id_controle_temperature = id_controle_temperature,
						            	id_collaborateur = id_collaborateur,
						            	id_appareil = id_appareil,
						            	first_name_collaborateur = first_name_collaborateur,
						            	last_name_collaborateur = last_name_collaborateur,
						            	name_appareil = name_appareil,
						            	location_appareil = location_appareil,
						            	temperature = temperature,
						            	periode_releve = periode_releve,
		    							description = description,
		    							user_username = request.user.get_username())

    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)
    	

    		    

	    
