from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import *
from .serializers import *
# Create your views here.


class CarModelView(ListCreateAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()


class ComplectationView(ListCreateAPIView):
    serializer_class = ComplectationSerializer
    queryset = Complectation.objects.all()


class CarView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CreditView(ListCreateAPIView):
    serializer_class = CreditSerializer
    queryset = Credit.objects.all()


class CalculatorView(ListCreateAPIView):
    serializer_class = CalculatorSerializer
    queryset = Calculator.objects.all()