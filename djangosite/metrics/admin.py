from django.contrib import admin
from .models import Location
from .models import Measurement
from .models import Timestamps


class TimestampAdmin(admin.ModelAdmin):
    list_display = ('pk', 'value', 'measurement', 'location', 'date', 'time',)
    list_filter = ('location', 'measurement',)


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'unit', 'description',)
    list_filter = ('name', 'unit',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'latitude', 'longitude',)
    list_filter = ('name', )


admin.site.register(Location, LocationAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Timestamps, TimestampAdmin)

# Register your models here.
