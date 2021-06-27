from django.urls import path
from . import views
from .views import BookingView, SingleBookingView, Booking_statusView, SingleBooking_statusView, BookingsDeleteView, \
    BookingsUpdateView, BookingsCreateView

app_name = "bookings"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name='index'),
    # path('delete/', views.delete, name='delete'),
    path('delete/<int:pk>', BookingsDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', BookingsUpdateView.as_view(), name='delete'),
    path('create/', BookingsCreateView.as_view(), name='delete'),
    path('api/bookings', BookingView.as_view()),
    path('api/bookings/<int:pk>', SingleBookingView.as_view()),
    path('api/booking_status', Booking_statusView.as_view()),
    path('api/booking_status/<int:pk>', SingleBooking_statusView.as_view())
]
