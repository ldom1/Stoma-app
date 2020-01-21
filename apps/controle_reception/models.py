from django.db import models

# Create your models here.
class ControleReception(models.Model):

    date = models.DateTimeField(null=True, blank=True)
    id_controle_reception = models.FloatField(null=True, blank=True)
    id_collaborateur = models.FloatField(null=True, blank=True)
    id_fournisseur = models.FloatField(null=True, blank=True)
    first_name_collaborateur = models.CharField(max_length=70, null=True, blank=True)
    last_name_collaborateur = models.CharField(max_length=70, null=True, blank=True)
    name_fournisseur = models.CharField(max_length=70, null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    periode_reception = models.CharField(max_length=70, null=True, blank=True)
    type_nourriture = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return "{0}".format(self.code, )