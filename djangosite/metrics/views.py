from django.shortcuts import render
from .models import Location
from .models import Measurement
from .models import Timestamps
from datetime import datetime
from django.db.models import Q
 
def index(request):
    locations = Location.objects.all()
    measurements = Measurement.objects.all()
    current_date = datetime.today()

    selected_location = request.GET.get("location")
    selected_measurement = request.GET.get("measurement")
    selected_date = request.GET.get("input_date")
    filter = Q()

    if str(selected_location) != 'None':
        filter &= Q(location__id=selected_location)

    if str(selected_measurement) != 'None':
        filter &= Q(measurement__id=selected_measurement)

    if str(selected_date) != 'None' and  str(selected_date) != "":
        filter &= Q(date=selected_date)
    print(type(selected_measurement))
    timestamps = Timestamps.objects.filter(filter).order_by('-date','time')
    
    return render(request, "index.html",{"locations": locations, "measurements": measurements,"timestamps": timestamps, "current_date":str(current_date)})