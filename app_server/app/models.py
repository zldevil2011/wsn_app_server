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


# Create your models here.
