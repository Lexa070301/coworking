from rest_framework import serializers
from .models import Space

#
# class SpaceSerializer(serializers.Serializer):
#     address = serializers.CharField(max_length=60)
#     capacity = serializers.IntegerField()
#     name = serializers.CharField(max_length=30)
#     area = serializers.IntegerField()
#     daily_cost = serializers.IntegerField()
#     description = serializers.CharField()
#     # feature = serializers.ManyRelatedField()
#
#     def create(self, validated_data):
#         return Space.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.address = validated_data.get('address', instance.address)
#         instance.capacity = validated_data.get('capacity', instance.capacity)
#         instance.name = validated_data.get('name', instance.name)
#         instance.area = validated_data.get('area', instance.area)
#         instance.daily_cost = validated_data.get('daily_cost', instance.daily_cost)
#         instance.description = validated_data.get('description', instance.description)
#         # instance.feature = validated_data.get('feature', instance.feature)
#         instance.save()
#         return instance
class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ('address', 'capacity', 'name', 'area', 'daily_cost', 'description');