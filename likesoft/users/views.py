from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializer import UserSerializer
from .tasks import send_welcome_email


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email)
        return Response(serializer.data)
