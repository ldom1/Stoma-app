from django.db import models

# Create your models here.
class Piece(models.Model):

    date = models.DateTimeField(null=True, blank=True)
    id_piece = models.FloatField(null=True, blank=True) 
    name_piece = models.CharField(max_length=70, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    user_username = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return "{0}".format(self.code, )