from django.urls import path
from . import views
from .views import UserView, SingleUserView

# app_name = "users"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('api/users', UserView.as_view()),
    path('api/users/<int:pk>', SingleUserView.as_view()),
]
