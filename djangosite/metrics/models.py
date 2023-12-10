from django.db import models
from datetime import date, time

from enum import Enum
from django import models

class MetricEnum(str, Enum):
    temp = "Temperature"
    feels_like = "Temperature Feels Like"
    temp_min = "Temperature Min"
    temp_max = "Temperature Max"
    pressure = "Pressure"
    humidity = "Humidity"
    wind_speed = "Wind Speed"
    wind_deg = "Wind Direction"
    rain_1h = "Rainfall in the Last Hour"
    snow_1h = "Snowfall in the Last Hour"
    clouds_all = "Cloud Coverage"
    weather_main = "Weather Main"

    @classmethod
    def choices(cls) -> tuple[tuple[str,str]]:
        return ((i.name, i.value) for i in cls)


class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Measurement(models.Model):
    name = models.CharField(max_length=255, choices=MetricEnum.choices())
    description= models.CharField(max_length=255, default='', blank=True)
    unit = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.get_name_display()} ({self.unit})"

class Timestamps(models.Model):
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=time(12, 0)) 


