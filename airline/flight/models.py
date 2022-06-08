from django.db import models

# Create your models here.
# how to create and nmanipulate tabales
#each mode is a python class
# you may have one model for eahc main table


class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duratin = models.IntegerField()

    def __str__(self):
        return self.origin + " - " + self.destination
