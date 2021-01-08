from django.contrib import admin
from import_export import resources
from .models import Space, Rating, Feature
from import_export.admin import ImportExportModelAdmin


class SpaceResource(resources.ModelResource):
    class Meta:
        model = Space


class RatingResource(resources.ModelResource):
    class Meta:
        model = Rating


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class SpaceAdmin(ImportExportModelAdmin):
    resource_class = SpaceResource


class RatingAdmin(ImportExportModelAdmin):
    resource_class = RatingResource


class FeatureAdmin(ImportExportModelAdmin):
    resource_class = FeatureResource


admin.site.register(Space, SpaceAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Feature, FeatureAdmin)
