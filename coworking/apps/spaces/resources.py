from import_export import resources
from .models import Space


class SpaceResource(resources.ModelResource):
    class Meta:
        model = Space
