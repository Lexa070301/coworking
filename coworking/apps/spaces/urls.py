from django.urls import path
from . import views
from .views import SpaceView, SingleSpaceView, RatingView, SingleRatingView, FeatureView, SingleFeatureView

app_name = "spaces"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name='index'),
    path('api/spaces', SpaceView.as_view()),
    path('api/spaces/<int:pk>', SingleSpaceView.as_view()),
    path('api/rating', RatingView.as_view()),
    path('api/rating/<int:pk>', SingleRatingView.as_view()),
    path('api/feature', FeatureView.as_view()),
    path('api/feature/<int:pk>', SingleFeatureView.as_view())
]
