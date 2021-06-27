from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Booking, Booking_status
from .serializers import BookingSerializer, Booking_statusSerializer


def index(request):
    bookings = Booking.objects.all()
    # features = Feature.objects.all()
    data = {
        'bookings': bookings,
        # 'features': features
    }
    return render(request, 'cabinet/bookings.html', data)

# def delete(request):
#     bookings = Booking.objects.all()
#     # features = Feature.objects.all()
#     data = {
#         'bookings': bookings,
#         # 'features': features
#     }
#     return render(request, 'cabinet/bookings.html', data)

# class BookingsDelete(DetailView):
#     # queryset = Space.objects.all()
#     model = Booking
#     template_name = 'cabinet/bookings.html'
#     context_object_name = 'bookings'

class BookingView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class SingleBookingView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class Booking_statusView(ListCreateAPIView):
    queryset = Booking_status.objects.all()
    serializer_class = Booking_statusSerializer


class SingleBooking_statusView(RetrieveUpdateDestroyAPIView):
    queryset = Booking_status.objects.all()
    serializer_class = Booking_statusSerializer