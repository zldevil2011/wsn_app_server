from django.shortcuts import render
from app.models import AppUser
from django.http import HttpResponse


def about_us(request):
    return render(request, 'about_us.html', {

    })
# Create your views here.
