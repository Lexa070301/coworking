from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'username', 'first_name', 'last_name', 'email', 'phone_number', 'user_role', 'is_staff', 'is_active', 'date_joined')
