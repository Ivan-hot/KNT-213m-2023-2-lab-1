from django.core.management.base import BaseCommand
import csv
import logging
from metrics.models import Measurement, Timestamps, MetricEnum
from datetime import datetime
from decimal import Decimal

logger = logging.getLogger(__name__)





class Command(BaseCommand):
    help = 'Creates django admin with provided arguments'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)

    def handle(self, *args, **options):
        fn = options.get('file')
        with open(fn, 'r') as f:
            __MAP = {}
            r = csv.DictReader(f, fieldnames=['datetime','count','holiday','workingday','temp','feels_like','temp_min','temp_max','pressure','humidity','wind_speed','wind_deg','rain_1h','snow_1h','clouds_all','weather_main'])
            __MAP[MetricEnum.temp.name], _ = Measurement.objects.get_or_create(name=MetricEnum.temp, unit='C')
            __MAP[MetricEnum.temp_min.name], _ = Measurement.objects.get_or_create(name=MetricEnum.temp_min, unit='C')
            __MAP[MetricEnum.temp_max.name], _ = Measurement.objects.get_or_create(name=MetricEnum.temp_max, unit='C')
            __MAP[MetricEnum.feels_like.name], _ = Measurement.objects.get_or_create(name=MetricEnum.feels_like, unit='C')
            __MAP[MetricEnum.pressure.name], _ = Measurement.objects.get_or_create(name=MetricEnum.pressure, unit='hPa')
            __MAP[MetricEnum.humidity.name], _ = Measurement.objects.get_or_create(name=MetricEnum.humidity, unit='%')
            __MAP[MetricEnum.wind_speed.name], _ = Measurement.objects.get_or_create(name=MetricEnum.wind_speed, unit='m/s')
            __MAP[MetricEnum.wind_deg.name], _ = Measurement.objects.get_or_create(name=MetricEnum.wind_deg, unit='degree')
            __MAP[MetricEnum.rain_1h.name], _ = Measurement.objects.get_or_create(name=MetricEnum.rain_1h, unit='mm/h')
            __MAP[MetricEnum.snow_1h.name], _ = Measurement.objects.get_or_create(name=MetricEnum.snow_1h, unit='mm/h')
            __MAP[MetricEnum.clouds_all.name], _ = Measurement.objects.get_or_create(name=MetricEnum.clouds_all, unit='%')
            __MAP[MetricEnum.weather_main.name], _ = Measurement.objects.get_or_create(name=MetricEnum.weather_main, unit='category')
            row_num = 0
            for row in r:
                row_num += 1
                if row_num == 1:
                    continue
                if row_num % 1000 == 0:
                    stdout = f'Saved rows: {row_num}'
                    self.stdout.write(self.style.SUCCESS(stdout))
                d, t = row['datetime'].split(' ')
                for i in MetricEnum:
                    Timestamps.objects.create(
                        value=str(row[i.name]) if row[i.name] is not None else '0.0', 
                        measurement = __MAP[i.name], 
                        date=d, 
                        time=t,
                    )
                
        stdout = f'File {fn} processed'
        self.stdout.write(self.style.SUCCESS(stdout))