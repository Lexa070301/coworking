from django.http import HttpResponse
from .models import Space


def index(request):
    space_features = Space.objects.filter(
        name='Райский остров'
    ).values('name', 'feature')
    return HttpResponse(space_features)
