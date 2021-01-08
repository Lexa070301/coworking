from rest_framework import serializers
from .models import Booking, Booking_status


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('start_date', 'end_date', 'space', 'user')


class Booking_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_status
        fields = ('status', 'booking')

