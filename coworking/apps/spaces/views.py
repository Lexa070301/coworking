from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.views.generic import DetailView
from .models import Space, Rating, Feature
from .serializers import SpaceSerializer, RatingSerializer, FeatureSerializer


def index(request):
    # spaces = Space.objects.all().order_by('-title')[:2]
    spaces = Space.objects.all()
    features = Feature.objects.all()
    data = {
        'spaces': spaces,
        'features': features
    }
    return render(request, 'spaces.html', data)


class SpaceDetailView(DetailView):
    # queryset = Space.objects.all()
    model = Space
    template_name = 'space.html'
    context_object_name = 'space'
    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the template context,
        now you can use {{ car }} within the template
        """
        context = super().get_context_data(**kwargs)
        context['rating'] = Rating.objects.all().order_by('-rating')
        return context


# class RatingDetailView(DetailView):
#     queryset = Rating.objects.all()
#     model = Rating
#     template_name = 'space.html'
#     context_object_name = 'rating'



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
