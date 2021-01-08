from django.contrib import admin
from import_export import resources
from .models import Booking, Booking_status
from import_export.admin import ImportExportModelAdmin


class BookingResource(resources.ModelResource):
    class Meta:
        model = Booking


class Booking_statusResource(resources.ModelResource):
    class Meta:
        model = Booking_status


class BookingAdmin(ImportExportModelAdmin):
    resource_class = BookingResource


class Booking_statusAdmin(ImportExportModelAdmin):
    resource_class = Booking_statusResource


admin.site.register(Booking, BookingAdmin)
admin.site.register(Booking_status, Booking_statusAdmin)
