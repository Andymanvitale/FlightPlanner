from django.db import models

class airportModel(models.Model):
    startApt = models.CharField(max_length=4, verbose_name= "Starting Airport")
    endApt = models.CharField(max_length=4, verbose_name= "Destination")