from djangosite import db as cachedb
from . import models
from datetime import date
from django.db.models import Q


def select_measurements():
    measurements = []
    try:
        measurements = cachedb.get_all_measurements()
    except Exception as e:
        print(f'Error was occurred while selecting measurements: {e}')
    finally:
        if not measurements:
            measurements = models.Measurement.objects.all()
    return measurements


def select_timestamps(selected_location=None, selected_measurement=None, selected_date=None):
    timestamps = []
    try:
        timestamps = cachedb.get_timestamp_by_params(
            location_id=selected_location, measurement_id=selected_measurement, date=selected_date)
        return timestamps
    except Exception as e:
        print(f'Error occured while selecting timestamps: {e}')
    finally:
        if not timestamps:
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
            timestamps = list(models.Timestamps.objects.filter(filter))
        return timestamps


def select_locations():
    locations = []
    try:
        locations = cachedb.get_all_locations()
    except Exception as e:
        print(f'Error occured while selecting locations: {e}')
    finally:
        if not locations:
            locations = models.Location.objects.all()
        return locations
