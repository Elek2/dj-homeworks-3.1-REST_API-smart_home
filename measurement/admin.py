from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'client']
    # inlines = [OrderPositionInline, ]
    # list_filter = ['category']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
