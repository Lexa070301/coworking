from django.contrib import admin
from import_export import resources
from .models import Payment, Payment_status
from import_export.admin import ImportExportModelAdmin


class PaymentResource(resources.ModelResource):
    class Meta:
        model = Payment


class Payment_statusResource(resources.ModelResource):
    class Meta:
        model = Payment_status


class PaymentAdmin(ImportExportModelAdmin):
    resource_class = PaymentResource


class Payment_statusAdmin(ImportExportModelAdmin):
    resource_class = Payment_statusResource


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Payment_status, Payment_statusAdmin)
