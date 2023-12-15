import datetime
import matplotlib
import matplotlib.pyplot as plt
from typing import TypedDict
from . import models
import io
import base64
from .model_for_classification.classify_data import classify_data
from collections import Counter
from djangosite.db import get_timestamp_by_params

matplotlib.use('Qt5Agg')
OptionalDate = datetime.date | None


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
    qs = get_timestamp_by_params(
        location_id=l, measurement_id=m, start_date=start_date, end_date=end_date)
    return tuple(
        qs
    )


def generate_metrics_plot(l: int, t: int, s: OptionalDate = None, e: OptionalDate = None):
    metrix = get_timestamps(l, t, s, e)
    datetimes = tuple(
        map(lambda m: datetime.datetime.strptime(m['date'] + " " + m['time'], '%Y-%m-%d %H:%M:%S'), metrix))
    if (len(metrix)):
        if metrix[0]["measurement"]["unit"] == "category":
            values = tuple(map(lambda m: m['value'], metrix))
        else:
            values = tuple(map(lambda m: float(m['value']), metrix))
    else:
        return None

    plt.useTkAgg = False
    images = []
    plt.clf()
    if (metrix[0]["measurement"]["unit"] == "category"):
        buffer = io.BytesIO()
        data_freq = Counter(values)
        unique_values = list(data_freq.keys())
        frequencies = list(data_freq.values())
        plt.xlabel('Values')
        plt.ylabel('Frequencies')
        plt.title('Historical Data Plot')
        plt.bar(unique_values, frequencies)
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        images.append(image_base64)
    else:
        buffer = io.BytesIO()
        plt.xlabel('Datetime')
        plt.ylabel('Values')
        plt.title('Historical Data Plot')
        plt.grid(True)
        plt.plot(datetimes, values, linestyle='-', marker='')
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        images.append(image_base64)

        plt.clf()
        buffer = io.BytesIO()
        plt.boxplot(values)
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        images.append(image_base64)

    return images


def classify_weather_by(measurements):
    return classify_data(measurements)
