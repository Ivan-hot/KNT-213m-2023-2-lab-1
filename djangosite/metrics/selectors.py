from djangosite import db as cachedb
from . import models


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


def select_timestamps(measurement_id: int | None = None, only_values: bool = False, flat: bool = False):
    timestamps = []
    try:
        timestamps = cachedb.get_all_timestamps()
    except Exception as e:
        print(f'Error occured while selecting timestamps: {e}')
    finally:
        if not timestamps:
            timestamps = list(models.Timestamps.objects.all())
            if measurement_id:
                timestamps = filter(lambda t: t.measurement_id == measurement_id, timestamps)
            if only_values:
                if flat:
                    timestamps = map(lambda t : t.value, timestamps)
                else:
                    timestamps = map(lambda t : {'value':t.value}, timestamps)
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
