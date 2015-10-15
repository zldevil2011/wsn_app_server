from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from app.models import Water
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from app.serializers import WaterSerializer
import datetime
import random
seed = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_-'


class WaterMethod(APIView):

    def get(self, request):
        water = Water.objects.all()
        serializer = WaterSerializer(water, many=True)
        return Response({"water": serializer.data}, status=status.HTTP_200_OK)