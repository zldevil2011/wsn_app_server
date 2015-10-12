from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from app.models import AppUser
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from app.serializers import RegisterSerializer
import datetime
import random
seed = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_-'

class Register(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = AppUser.objects.get(email=serializer.data['email'])
                admin_user = User.objects.get(email=serializer.data['email'])
                return Response({"status": "user exist"},status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                username = ""
                num = random.randint(4, 10)
                while True:
                    username = ""
                    for i in range(num):
                        username += random.choice(seed)
                    try:
                        user = AppUser.objects.get(username=username)
                    except AppUser.DoesNotExist:
                        break
                password = serializer.data['password']
                email = serializer.data['email']
                admin_user = User.objects.create_user(username=username, password=password,
                                                      last_login=datetime.datetime.now(), email=email)
                admin_user.save()
                user = AppUser()
                user.username = username
                user.password = password
                user.user = admin_user
                user.email = email
                user.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response({"status": "format error"}, status=status.HTTP_400_BAD_REQUEST)