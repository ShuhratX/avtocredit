from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import *
from rest_framework.response import Response
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
    serializer_class = CompareSerializer
    queryset = Car.objects.all()

    def post(self, request):
        car1 = request.data.get('car1')
        car2 = request.data.get('car2')
        cars = []
        if car1 and car2:
            comps = [car1, car2]
            for comp in comps:
                car = Car.objects.filter(complectation=comp)
                if car:
                    cars.append({
                        "model": car.model.name,
                        "complectation": car.complectation,
                        "price": car.price,
                        "color": car.color,
                        "power": car.power,
                        "fuel_type": car.fuel_type,
                        "transmission": car.transmission,
                        "top_speed": car.top_speed,
                    })
                else:
                    cars = ["Mavjud bo'lmagan avto"]
            return Response(cars)
        else:
            return Response("Ikkita mashina tanlang!")
