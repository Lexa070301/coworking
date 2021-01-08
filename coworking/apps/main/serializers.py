from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')


# class Payment_statusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment_status
#         fields = ('status', 'payment')