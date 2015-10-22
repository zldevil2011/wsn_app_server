from rest_framework import serializers
from app.models import AppUser, News, Air, Water, Weather, Device


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


class AirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Air
        fields = ('air_id', 'pm25', 'cloud', 'rain', 'ziwai', 'guang', 'clouddir', 'time')


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('weather_id', 'tem', 'wea', 'humidity', 'cloud_speed', 'week', 'lunnar', 'time')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id', 'device_name', 'device_maker', 'device_price', 'device_photo', 'device_desc')
