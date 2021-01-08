from django.urls import path
from . import views
from .views import BookingView, SingleBookingView, Booking_statusView, SingleBooking_statusView

app_name = "bookings"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name='index'),
    path('api/bookings', BookingView.as_view()),
    path('api/bookings/<int:pk>', SingleBookingView.as_view()),
    path('api/booking_status', Booking_statusView.as_view()),
    path('api/booking_status/<int:pk>', SingleBooking_statusView.as_view())
]
