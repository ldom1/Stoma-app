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


@login_required
def view_display_appareil(request):

    appareil = Appareil.objects.filter(user_username=request.user.get_username())

    id_appareil = request.GET.get('get_id')

    if id_appareil:

	    appareil_to_delete = appareil.filter(id_appareil=id_appareil)
	    for ap in appareil_to_delete:
	    	ap.delete()

    context = {'appareil': appareil}

    return render(request, 'appareil/display_appareil.html', context)

class view_register_appareil(TemplateView):
	# Form to get data
    template_name = 'appareil/register_appareil.html'

    def get(self, request):
    	context = {}

    	form = appareilForm()
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}
    	form = appareilForm(request.POST)

    	if form.is_valid():

    		name = form.cleaned_data['name']
    		location = form.cleaned_data['location']
    		description = form.cleaned_data['description']

    		# Get the id
    		appareil = Appareil.objects.filter(user_username=request.user.get_username())

    		try:
    			id_appareil = np.int(np.max([y.id_appareil for y in appareil]) + 1)
    		except Exception:
    			id_appareil = 1
    		asset, created = Appareil.objects.get_or_create(
				            	date = datetime.datetime.today(),
				            	name = name,
				            	id_appareil = id_appareil,
				            	location=location,
    							description = description,
    							user_username = request.user.get_username())
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)
