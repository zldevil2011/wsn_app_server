# -*- coding:utf-8 -*-
from django.contrib import admin
from app.models import AppUser, Air, News, Water, Weather, Device


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user')


class AirAdmin(admin.ModelAdmin):
    list_display = ('air_id', 'time')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'news_title')


class WaterAdmin(admin.ModelAdmin):
    list_display = ('water_id', 'time')


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('weather_id', 'time')


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'device_name')


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Air, AirAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Water, WaterAdmin)
admin.site.register(Weather, WeatherAdmin)
admin.site.register(Device, DeviceAdmin)
# Register your models here.
