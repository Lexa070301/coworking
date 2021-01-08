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

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class BookingAdmin(ImportExportModelAdmin):
    resource_class = BookingResource
    list_display = ('start_date', 'end_date', 'space', 'user',)
    search_fields = ('start_date', 'end_date')
    filter_horizontal = ()
    list_filter = ('start_date', 'end_date', 'space', 'user')
    fieldsets = ()


class Booking_statusAdmin(ImportExportModelAdmin):
    resource_class = Booking_statusResource
    list_display = ('status', 'booking')
    search_fields = (['status'])
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Booking, BookingAdmin)
admin.site.register(Booking_status, Booking_statusAdmin)
