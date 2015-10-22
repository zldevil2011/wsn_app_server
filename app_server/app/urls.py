"""app_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from api.user.register import Register
from api.data.water import WaterMethod
from api.data.air import AirMethod
from api.data.weather import WeatherMethod
from api.data.device import DeviceMethod
from views import about_us
urlpatterns = patterns('',
                       url(r'^about_us', about_us, name="about_us"),
                       url(r'^user/register', csrf_exempt(Register.as_view())),
                       url(r'^data/water/', (WaterMethod.as_view())),
                       url(r'^data/air/', (AirMethod.as_view())),
                       url(r'^data/weather/', (WeatherMethod.as_view())),
                       url(r'^data/device/', (DeviceMethod.as_view())),
                       )
