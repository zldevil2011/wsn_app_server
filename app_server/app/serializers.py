from rest_framework import serializers
from app.models import AppUser, News, Air, Water


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'password', 'name', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('email', 'password')


class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ('water_id', 'ph', 'do', 'turbidity', 'water_level', 'conductivity', 'time')
