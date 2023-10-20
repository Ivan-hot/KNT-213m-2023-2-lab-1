from django.shortcuts import render
from .models import Location
from .models import Measurement
 
def index(request):
    locations = Location.objects.all()
    measurements = Measurement.objects.all()
    print(measurements)
    return render(request, "index.html",{"locations": locations, "measurements": measurements})