from django.contrib import admin
from import_export import resources
from .models import Space, Rating, Feature
from import_export.admin import ImportExportModelAdmin


class SpaceResource(resources.ModelResource):
    class Meta:
        model = Space


class SpaceAdmin(ImportExportModelAdmin):
    resource_class = SpaceResource


admin.site.register(Space, SpaceAdmin)
admin.site.register(Rating)
admin.site.register(Feature)
