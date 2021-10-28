from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import *
from .serializers import *
# Create your views here.

class CarView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()