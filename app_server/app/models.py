# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20, default="None")
    email = models.EmailField(null=True)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return str(self.username)


class Air(models.Model):
    air_id = models.AutoField(primary_key=True)
    pm25 = models.FloatField(default=0)
    cloud = models.FloatField(default=0)
    rain = models.FloatField(default=0)
    ziwai = models.FloatField(default=0)
    guang = models.FloatField(default=0)
    clouddir = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __unicode__(self):
        return str(self.air_id)


class Water(models.Model):
    water_id = models.AutoField(primary_key=True)
    ph = models.FloatField(default=0)
    do = models.FloatField(default=0)
    turbidity = models.FloatField(default=0)
    water_level = models.FloatField(default=0)
    conductivity = models.FloatField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.water_id)


class Weather(models.Model):
    weather_id = models.AutoField(primary_key=True)
    tem = models.FloatField(default=0.0)
    wea = models.CharField(max_length=200)
    humidity = models.FloatField(default=0.0)
    cloud_speed = models.FloatField(default=0.0)
    week = models.CharField(max_length=200)
    lunnar = models.CharField(max_length=200)
    time = models.DateField(null=True)

    def __unicode__(self):
        return str(self.weather_id)


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=200)
    news_type = models.IntegerField()
    news_content = models.CharField(max_length=10000)
    news_update_time = models.CharField(max_length=200)
    news_priori = models.IntegerField(default=0)
    news_readtime = models.IntegerField(default=0)
    news_author = models.ForeignKey(AppUser, related_name='news', null=True)

    def __unicode__(self):
        return str(self.news_id)


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=200, null=True, default="设备名称")
    device_maker = models.CharField(max_length=200, null=True, default="设备制造商")
    device_price = models.FloatField(default=0)
    device_photo = models.URLField(null=True, default="http://120.27.35.194:8080/camera.png")
    device_desc = models.CharField(max_length=10000, null=True, default="设备详情描述")

    def __unicode__(self):
        return str(self.device_id)
# Create your models here.
