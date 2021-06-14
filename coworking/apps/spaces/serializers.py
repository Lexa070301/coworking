from rest_framework import serializers
from .models import Space, Rating, Feature


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ('address', 'capacity', 'name', 'area', 'daily_cost', 'description', 'feature')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating', 'review', 'space', 'user')


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = (['feature'])
