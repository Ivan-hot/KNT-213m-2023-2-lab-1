from django.db import models
from datetime import date, time

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longtitude = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Unit_Mesure(models.Model):
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.description})"

class Measurement(models.Model):
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    unit = models.ForeignKey(Unit_Mesure,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.unit.name})"

class Timestamps(models.Model):
    measurement = models.ForeignKey(Measurement,on_delete=models.CASCADE)
    value = models.FloatField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=time(12, 0)) 

    def __str__(self):
        return f"{self.id} {self.measurement.name} {self.location.name}"


