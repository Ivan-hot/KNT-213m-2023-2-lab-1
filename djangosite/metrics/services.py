import datetime
import matplotlib
import matplotlib.pyplot as plt
from typing import TypedDict
from . import models
from os.path import join
from django.conf import settings
from .model_for_classification.classify_data import classify_data

matplotlib.use('Qt5Agg')
OptionalDate = datetime.date | None

file_image = "image_measurement.png"


class TimestampMetrics(TypedDict):
    value: str
    date: datetime.date
    time: datetime.time


def get_timestamps(
    l: int,
    m: int,
    start_date: OptionalDate = None,
    end_date: OptionalDate = None
) -> tuple[TimestampMetrics]:
    qs = models.Timestamps.objects \
        .filter(measurement__id=m, location__id=l) \
        .values('value', 'date', 'time')
    if (start_date is not None):
        qs = qs.filter(date__gte=start_date)
    if (start_date is not None):
        qs = qs.filter(date__lte=end_date)
    return tuple(
        qs
    )


def generate_metrics_plot(l: int, t: int, s: OptionalDate = None, e: OptionalDate = None):
    metrix = get_timestamps(l, t)
    datetimes = tuple(
        map(lambda m: datetime.datetime.combine(m['date'], m['time']), metrix))
    if t == models.MetricEnum.weather_main:
        values = tuple(map(lambda m: m['value'], metrix))
    else:
        values = tuple(map(lambda m: float(m['value']), metrix))

    plt.useTkAgg = False
    plt.xlabel('Datetime')
    plt.ylabel('Values')
    plt.title('Historical Data Plot')
    plt.grid(True)
    plt.plot(datetimes, values)
    plt.savefig("./media/" + file_image, format='png')

    return file_image


def classify_weather_by(measurements):
    return classify_data(measurements)
