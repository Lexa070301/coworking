from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Space, Rating, Feature
from .serializers import SpaceSerializer, RatingSerializer, FeatureSerializer



def index(request):
    return HttpResponse('Spaces works!')


class SpaceView(ListCreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class SingleSpaceView(RetrieveUpdateDestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class RatingView(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class SingleRatingView(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FeatureView(ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class SingleFeatureView(RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
