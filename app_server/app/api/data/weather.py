from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Weather
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from app.serializers import WeatherSerializer
import datetime
import random
seed = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_-'


class WeatherMethod(APIView):

    def get(self, request):
        weather = Weather.objects.all()[0:1]
        serializer = WeatherSerializer(weather, many=True)
        return Response({"weather": serializer.data}, status=status.HTTP_200_OK)