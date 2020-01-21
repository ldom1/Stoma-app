from django.db import models

# Create your models here.
class ControleTemperature(models.Model):

    date = models.DateTimeField(null=True, blank=True)
    id_controle_temperature = models.FloatField(null=True, blank=True)
    id_collaborateur = models.FloatField(null=True, blank=True)
    id_appareil = models.FloatField(null=True, blank=True)
    first_name_collaborateur = models.CharField(max_length=70, null=True, blank=True)
    last_name_collaborateur = models.CharField(max_length=70, null=True, blank=True)
    name_appareil = models.CharField(max_length=70, null=True, blank=True)
    location_appareil = models.CharField(max_length=70, null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    periode_releve = models.CharField(max_length=70, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return "{0}".format(self.code, )