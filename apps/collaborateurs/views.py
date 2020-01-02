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
def view_display_collaborateur(request):

    collaborateur = Collaborateur.objects.filter(user_username=request.user.get_username())

    id_collaborateur = request.GET.get('get_id')

    if id_collaborateur:

	    collaborateur_to_delete = collaborateur.filter(id_collaborateur=id_collaborateur)
	    for collab in collaborateur_to_delete:
	    	collab.delete()

    context = {'collaborateur': collaborateur}

    return render(request, 'collaborateurs/display_collaborateurs.html', context)

class view_register_collaborateur(TemplateView):
	# Form to get data
    template_name = 'collaborateurs/register_collaborateurs.html'

    def get(self, request):
    	context = {}

    	form = collaborateurForm()
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}
    	form = collaborateurForm(request.POST)

    	if form.is_valid():

    		first_name = form.cleaned_data['first_name']
    		last_name = form.cleaned_data['last_name']
    		description = form.cleaned_data['description']

    		# Get the id
    		collaborateur = Collaborateur.objects.filter(user_username=request.user.get_username())

    		try:
    			id_collaborateur = np.int(np.max([y.id_collaborateur for y in collaborateur]) + 1)
    		except Exception:
    			id_collaborateur = 1
    		asset, created = Collaborateur.objects.get_or_create(
				            	first_name = first_name,
				            	last_name = last_name,
				            	date = datetime.datetime.today(),
				            	id_collaborateur = id_collaborateur,
    							description = description,
    							user_username = request.user.get_username())
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)
