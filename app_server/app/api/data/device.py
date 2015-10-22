from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Device
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from app.serializers import DeviceSerializer
import datetime
import random
seed = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_-'


class DeviceMethod(APIView):

    def get(self, request):
        device = Device.objects.all()
        serializer = DeviceSerializer(device, many=True)
        return Response({"device": serializer.data}, status=status.HTTP_200_OK)