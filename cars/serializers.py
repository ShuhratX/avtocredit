from django.db.models import fields
from rest_framework import serializers
from .models import *


class CalculatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculator
        fields = ("id", "order", "sum", "percent", "total", "remain")


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        fields = ('status',)


class CreditSerializer(serializers.ModelSerializer):
    payments = CalculatorSerializer(required=False, many=True)  
    class Meta:
        model = Credit
        fields = ("month", "payments")


class CompareSerializer(serializers.Serializer):
    complectation1 = serializers.CharField(max_length=100)
    complectation2 = serializers.CharField(max_length=100)


class CarSerializer(serializers.ModelSerializer):
    credit = CreditSerializer(required=False, many=True)
    class Meta:
        model = Car
        fields = ("id", "title", "credit")


class CarModelSerializer(serializers.ModelSerializer):
    models = CarSerializer(required=False, many=True)
    class Meta:
        model = CarModel
        fields = ("id", "title", "models")
