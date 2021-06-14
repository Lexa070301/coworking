from django.contrib import admin
from import_export import resources
from django.contrib.auth.admin import Group
from .models import User
from import_export.admin import ImportExportModelAdmin


class AccountResource(resources.ModelResource):
    class Meta:
        model = User


class AccountAdmin(ImportExportModelAdmin):
    resource_class = AccountResource
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_active', 'date_joined')
    fieldsets = ()


admin.site.unregister(Group)
admin.site.register(User, AccountAdmin)
