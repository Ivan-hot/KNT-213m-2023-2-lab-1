import datetime
import matplotlib
import matplotlib.pyplot as plt
from typing import TypedDict
from . import models

matplotlib.use('Qt5Agg')
OptionalDate = datetime.date | None


class TimestampMetrics(TypedDict):
    value: str
    date: datetime.date
    time: datetime.time


def get_timestamps_by_measure(
    m: models.MetricEnum, 
    start_date: OptionalDate = None, 
    end_date: OptionalDate = None
) -> tuple[TimestampMetrics]:
    mes = models.Measurement.objects.get(name=m)
    qs =models.Timestamps.objects \
            .filter(measurement=mes) \
            .values('value', 'date', 'time')
    if (start_date is not None):
        qs = qs.filter(date__gte=start_date)
    if (start_date is not None):
        qs = qs.filter(date__lte=end_date)
    return tuple(
        qs
    )


def generate_metrics_plot(t: models.MetricEnum, s: OptionalDate = None, e: OptionalDate = None):
    metrix = get_timestamps_by_measure(t)
    datetimes = tuple(map(lambda m: datetime.datetime.combine(m['date'],m['time']), metrix))
    if t == models.MetricEnum.weather_main:
        values = tuple(map(lambda m: m['value'], metrix))
    else:
        values = tuple(map(lambda m: float(m['value']), metrix))
    plt.plot(datetimes, values)
    plt.savefig(f'{t}_{s}-{e}', format='png')

