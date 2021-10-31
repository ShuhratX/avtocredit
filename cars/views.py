from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import *
from .serializers import *
import django_filters
from rest_framework import filters
# Create your views here.


class CarModelView(ListCreateAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()


class CarView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['complectation',]
    filter_fields = ['color', 'price',]


class CreditView(ListCreateAPIView):
    serializer_class = CreditSerializer
    queryset = Credit.objects.all()


class CalculatorView(ListCreateAPIView):
    serializer_class = CalculatorSerializer
    queryset = Calculator.objects.all()


class ComparisonView(GenericAPIView):
    serializer_class = CarSerializer