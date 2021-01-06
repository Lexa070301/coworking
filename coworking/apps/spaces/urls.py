from django.urls import path
from . import views
from .views import SpaceView, SingleSpaceView


app_name = "spaces"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', SpaceView.as_view()),
    path('api/<int:pk>', SingleSpaceView.as_view())
]