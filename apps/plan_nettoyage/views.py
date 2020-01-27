from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.apps import apps
from datetime import datetime, date, timedelta

from .models import *
from .utils import *
from .forms import *


class PlanNettoyageView(generic.ListView):
    model = PlanNettoyage
    template_name = 'plan_nettoyage/calendrier_plan_nettoyage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = PlanNettoyage()
    if event_id:
        instance = get_object_or_404(PlanNettoyage, pk=event_id)
    else:
        instance = PlanNettoyage()

    form = PlanNettoyageForm(request.POST or None, instance=instance)

    if request.POST and form.is_valid():

    	title = form.cleaned_data['title']
    	start_time = form.cleaned_data['start_time']
    	end_time = form.cleaned_data['end_time']
    	first_name_collaborateur = form.cleaned_data['first_name_collaborateur']
    	last_name_collaborateur = form.cleaned_data['last_name_collaborateur']
    	#piece = form.cleaned_data['piece']
    	description = form.cleaned_data['description']

    	# Get the id
    	plan_nettoyage = PlanNettoyage.objects.filter(user_username=request.user.get_username())
    	id_collaborateur = apps.get_model('collaborateurs', 'Collaborateur').objects.filter(user_username=request.user.get_username(),
																						   first_name = first_name_collaborateur,
																						   last_name = last_name_collaborateur,)[0].id_collaborateur
    	try:
    		id_plan_nettoyage = np.int(np.max([y.id_plan_nettoyage for y in plan_nettoyage]) + 1)
    	except Exception:
    		id_plan_nettoyage = 1

    	asset, created = PlanNettoyage.objects.get_or_create(
					            	date = datetime.today(),
					            	title=title,
					            	id_plan_nettoyage = id_plan_nettoyage,
					            	id_collaborateur = id_collaborateur,
					            	start_time = start_time,
					            	end_time = end_time,
					            	first_name_collaborateur = first_name_collaborateur,
					            	last_name_collaborateur = last_name_collaborateur,
					            	piece = piece,
	    							description = description,
	    							user_username = request.user.get_username())

    	return HttpResponseRedirect(reverse('calendrier_plan_nettoyage'))
    return render(request, 'plan_nettoyage/events.html', {'form': form})
