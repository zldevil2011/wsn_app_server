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

# Create your models here.
