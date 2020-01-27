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
def view_display_piece(request):

    piece = Piece.objects.filter(user_username=request.user.get_username())

    id_piece = request.GET.get('get_id')

    if id_piece:

	    piece_to_delete = piece.filter(id_appareil=id_piece)
	    for p in piece_to_delete:
	    	p.delete()

    context = {'piece': piece}

    return render(request, 'piece/display_piece.html', context)

class view_register_piece(TemplateView):
	# Form to get data
    template_name = 'piece/register_piece.html'

    def get(self, request):
    	context = {}

    	form = pieceForm()
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)

    def post(self, request):
    	context = {}
    	form = pieceForm(request.POST)

    	if form.is_valid():

    		name_piece = form.cleaned_data['name_piece']
    		description = form.cleaned_data['description']

    		# Get the id
    		piece = Piece.objects.filter(user_username=request.user.get_username())

    		try:
    			id_piece = np.int(np.max([y.id_piece for y in piece]) + 1)
    		except Exception:
    			id_piece = 1
    		asset, created = Piece.objects.get_or_create(
				            	date = datetime.datetime.today(),
				            	name_piece = name_piece,
				            	id_piece = id_piece,
    							description = description,
    							user_username = request.user.get_username())
    	# context
    	context['form'] = form
    	return render(request, self.template_name, context)
