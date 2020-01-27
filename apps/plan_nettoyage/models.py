from django.db import models
from django.urls import reverse

class PlanNettoyage(models.Model):

	title = models.CharField(max_length=200,  null=True, blank=True)
	date = models.DateTimeField(null=True, blank=True)
	id_plan_nettoyage = models.FloatField(null=True, blank=True)
	description = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	id_collaborateur = models.FloatField(null=True, blank=True)
	first_name_collaborateur = models.CharField(max_length=70, null=True, blank=True)
	last_name_collaborateur = models.CharField(max_length=70, null=True, blank=True)
	piece = models.CharField(max_length=70, null=True, blank=True)
	user_username = models.CharField(max_length=150, null=True, blank=True)

	@property
	def get_html_url(self):
		url = reverse('event_edit', args=(self.id,))
		return f'<a href="{url}"> {self.title} </a>'
