from rest_framework import serializers
from .models import Payment, Payment_status


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('date', 'size', 'booking', 'user')


class Payment_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_status
        fields = ('status', 'payment')
