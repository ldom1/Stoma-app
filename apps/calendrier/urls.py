from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('calendrier/', views.CalendarView.as_view(), name='calendrier'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]