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
from .services import generate_metrics_plot
from django.db.models import Min, Max


def main_index(request):
    locations = Location.objects.all()
    measurements = Measurement.objects.all()
    current_date = datetime.today()

    selected_location = int(request.GET.get("location", 0))
    selected_measurement = int(request.GET.get("measurement", 0))
    selected_date = request.GET.get("input_date", current_date)
    filter = Q()

    if selected_location:
        print("true")
        filter &= Q(location__id=selected_location)
    else:
        selected_location = 0

    if selected_measurement:
        filter &= Q(measurement__id=selected_measurement)
    else:
        selected_measurement = 0

    filter &= Q(date=selected_date)

    timestamps = Timestamps.objects.filter(filter).order_by('-date', 'time')

    return render(request, "./main/index.html", {"locations": locations, "measurements": measurements, "timestamps": timestamps, "current_date": str(current_date),
                                                 "selected_location": int(selected_location), "selected_measurement": int(selected_measurement), "selected_date": str(selected_date)})


def analysis_index(request):
    locations = Location.objects.all()
    measurements = Measurement.objects.all()
    current_date = datetime.today()

    selected_location = int(request.GET.get("location", 0))
    selected_measurement = int(request.GET.get("measurement", 0))
    selected_date_from = request.GET.get("date_from", current_date)
    selected_date_to = request.GET.get("date_to", current_date)

    if selected_measurement:
        generate_metrics_plot(selected_measurement,
                              selected_date_from, selected_date_to)

    return render(request, "./analysis/index.html", {"locations": locations, "measurements": measurements, "current_date": str(current_date), "selected_date_to": str(selected_date_to), "selected_date_from": str(selected_date_from),  "selected_location": int(selected_location), "selected_measurement": int(selected_measurement)})


def classification_index(request):
    measurements = Measurement.objects.all()
    form_data = []
    for measurement in measurements:
        if measurement.unit != 'category':
            print(measurement.name)
            min_value = Timestamps.objects.filter(
                measurement__id=measurement.id).order_by("value").first().value
            print(min_value)
    return render(request, "./classification/index.html", {})


@decorators.api_view(['post'])
@transaction.atomic
def timeStamps(request: Request):
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
