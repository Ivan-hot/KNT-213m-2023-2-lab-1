from django.contrib import admin
from .models import Location
from .models import Unit_Mesure
from .models import Measurement
from .models import Timestamps

admin.site.register(Location)
admin.site.register(Unit_Mesure)
admin.site.register(Measurement)
admin.site.register(Timestamps)

# Register your models here.
