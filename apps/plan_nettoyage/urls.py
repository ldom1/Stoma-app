from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('calendrier_plan_nettoyage/', views.PlanNettoyageView.as_view(), name='calendrier_plan_nettoyage'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]