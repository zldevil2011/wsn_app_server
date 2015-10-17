from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from app.models import Air
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from app.serializers import AirSerializer
import datetime
import random
seed = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_-'


class AirMethod(APIView):

    def get(self, request):
        air = Air.objects.all()
        serializer = AirSerializer(air, many=True)
        return Response({"air": serializer.data}, status=status.HTTP_200_OK)
