from django.db import models

# Create your models here.
# how to create and nmanipulate tabales
#each mode is a python class
# you may have one model for eahc main table

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.origin} -  {self.destination}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name = "departures")
    #using the keyword sdeparture we can access all the flights that are leavign from that airport
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name = "arrivals")
    duratin = models.IntegerField()

    def __str__(self):
        return self.origin + " - " + self.destination
