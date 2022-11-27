from django.db import models

class airportModel(models.Model):
    startApt = models.CharField(max_length=3)
    endApt = models.CharField(max_length=3)