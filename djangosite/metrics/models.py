from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    logtitude = models.FloatField()
    altitude = models.FloatField()

class Unit_Mesure(models.Model):
    name = models.CharField(max_length=255)

class Measurement(models.Model):
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    unit = models.ForeignKey(Unit_Mesure,on_delete=models.CASCADE)

class Timestamps(models.Model):
    measurement = models.ForeignKey(Measurement,on_delete=models.CASCADE)
    value = models.FloatField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    time = models.DateTimeField()

