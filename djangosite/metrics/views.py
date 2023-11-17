from django.shortcuts import render
from .models import Location
from .models import Measurement
from .models import Timestamps
from datetime import datetime
from django.db.models import Q
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import transaction
from services import generate_metrics_plot

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

def index_pre(request):
    locations = Location.objects.all()
    measurements = Measurement.objects.all()
    current_date = datetime.today()

    selected_location = request.GET.get("location")
    selected_measurement = request.GET.get("measurement")
    selected_date_from = request.GET.get("date_from")
    selected_date_to = request.GET.get("date_to")

    generate_metrics_plot(selected_measurement, selected_date_from, selected_date_to)

    return render(request, "index_pre.html",{"locations": locations, "measurements": measurements, "current_date":str(current_date)})

@decorators.api_view(['post'])
@transaction.atomic
def timeStamps(request:Request):
    for timestamp in request.data: 
        location = timestamp.get("location")
        locObject, _ = Location.objects.get_or_create(**location)
        date = timestamp.get("date")
        time = timestamp.get("time")
        for measurement in timestamp.get("measurment"):
            measObject, _ = Measurement.objects.get_or_create(
                name=measurement.get("name"),
                defaults={
                    "description": measurement.get("description"),
                    "unit": measurement.get("unitName"),
                })
            Timestamps.objects.create(
                measurement=measObject, 
                location=locObject, 
                date=date, 
                time=time, 
                value=measurement.get("value"),
            )
    return Response()
            
