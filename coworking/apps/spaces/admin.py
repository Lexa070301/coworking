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


def plus_cost(modeladmin, request, queryset):
    queryset.update(daily_cost=0)


plus_cost.short_description = 'Обнулить'


class SpaceAdmin(ImportExportModelAdmin):
    resource_class = SpaceResource
    list_display = ('name', 'address', 'capacity', 'area', 'daily_cost', 'description')
    search_fields = ('name', 'address', 'description')
    filter_horizontal = ()
    list_filter = ('name', 'address', 'capacity', 'area', 'daily_cost')
    fieldsets = ()
    actions = [plus_cost]


class RatingAdmin(ImportExportModelAdmin):
    resource_class = RatingResource
    list_display = ('rating', 'review', 'space', 'user')
    search_fields = (['review'])
    filter_horizontal = ()
    list_filter = (['rating'])
    fieldsets = ()


class FeatureAdmin(ImportExportModelAdmin):
    resource_class = FeatureResource
    list_display = (['feature'])
    search_fields = (['feature'])
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Space, SpaceAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Feature, FeatureAdmin)
