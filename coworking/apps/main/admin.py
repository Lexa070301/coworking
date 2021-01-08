# from django.contrib import admin
# from import_export import resources
# from import_export.admin import ExportMixin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from import_export.admin import ImportExportModelAdmin
#
#
# class UserResource(resources.ModelResource):
#     class Meta:
#         model = User
#
#
# # class UserAdmin(ImportExportModelAdmin):
# #     resource_class = UserResource
# class NewUserAdmin(ExportMixin, UserAdmin):
#     resource_class = UserResource
#     pass
#
#
# admin.site.unregister(User)
# admin.site.register(User, NewUserAdmin)
# # admin.site.register(Rating, RatingAdmin)
# # admin.site.register(Feature, FeatureAdmin)
