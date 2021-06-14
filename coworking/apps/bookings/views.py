from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Booking, Booking_status
from .serializers import BookingSerializer, Booking_statusSerializer


def index(request):
    return HttpResponse('Bookings works!')


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