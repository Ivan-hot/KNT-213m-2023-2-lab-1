from django.shortcuts import render, redirect
from .models import Location
from .models import Measurement
from .models import Timestamps
from datetime import datetime
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import transaction
from .services import generate_metrics_plot, classify_weather_by
import numpy as np
from .forms import TimestampEntryForm, LocationEntryForm, MeasurementEntryForm


def data_index(request):
    options = ["Timestamps", "Location", "Measurement"]
    selected_model = request.GET.get("model", "Timestamps")
    if selected_model == "Timestamps":
        form_class = TimestampEntryForm
    elif selected_model == "Location":
        form_class = LocationEntryForm
    else:
        form_class = MeasurementEntryForm
    message = ''
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            message = "Data has been successfully added"
            form = form_class()
        else:
            message = "Data is not valid"
    else:
        form = form_class()
    print(selected_model)
    return render(request, "./data/index.html", {'form': form, 'message': message, "selected_model": selected_model, "options": options})


def main_index(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['get'])
    try:
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

        timestamps = Timestamps.objects.filter(
            filter).order_by('-date', 'time')

        return render(request, "./main/index.html", {"locations": locations, "measurements": measurements, "timestamps": timestamps, "current_date": str(current_date), "selected_location": int(selected_location), "selected_measurement": int(selected_measurement), "selected_date": str(selected_date)}, status=200)
    except Exception as e:
        return render(request, "error_template.html", {"error_message": str(e)}, status=500)


def analysis_index(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['get'])

    try:
        locations = Location.objects.all()
        measurements = Measurement.objects.all()
        current_date = datetime.today()

        selected_location = int(request.GET.get("location", 0))
        selected_measurement = int(request.GET.get("measurement", 0))
        selected_date_from = request.GET.get("date_from", current_date)
        selected_date_to = request.GET.get("date_to", current_date)

        if selected_measurement and selected_location:
            images = generate_metrics_plot(selected_location, selected_measurement,
                                           selected_date_from, selected_date_to)
        else:
            images = []

        return render(request, "./analysis/index.html", {"locations": locations, "measurements": measurements, "current_date": str(current_date), "selected_date_to": str(selected_date_to), "selected_date_from": str(selected_date_from),  "selected_location": int(selected_location), "selected_measurement": int(selected_measurement), "images": images})
    except Exception as e:
        return render(request, "error_template.html", {"error_message": str(e)}, status=500)


def classification_index(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['get'])
    try:
        query_params = request.GET
        if len(query_params):
            arr_data = []
            for key, value in query_params.items():
                arr_data.append(float(value))
            arr_data = np.array(arr_data).reshape(1, -1)
            result, message = classify_weather_by(arr_data)
        else:
            result = ''
            message = ''
        measurements = Measurement.objects.all()
        form_data = []
        for measurement in measurements:
            if measurement.unit != 'category':
                values = Timestamps.objects.filter(
                    measurement__id=measurement.id).values_list('value', flat=True)
                float_values = [
                    float(value) if value is not None and value != '' else 0 for value in values]
                float_values.sort()
                min_value = float_values[0]
                max_value = float_values[-1]
                num_steps = 1000
                step = (max_value - min_value) / num_steps
                value = query_params.get(
                    str(measurement.id)) if query_params else None
                form_data.append(
                    {"measurement": measurement, "min_value": min_value, "max_value": max_value, "step": step, "value": value})

            return render(request, "./classification/index.html", {"form_data": form_data, "result": result, "message": message})
    except Exception as e:
        return render(request, "error_template.html", {"error_message": str(e)}, status=500)


@decorators.api_view(['post'])
@transaction.atomic
def timeStamps(request: Request) -> Response:
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
