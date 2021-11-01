from django.db.models import fields
from rest_framework import serializers
from .models import *

class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer(required=False, many=False)
    class Meta:
        model = Car
        fields = "__all__"


class CalculatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculator
        fields = "__all__"


class CreditSerializer(serializers.ModelSerializer):
    model = CarModelSerializer(required=False, many=False)
    calculator = CalculatorSerializer(required=False, many=True)  
    class Meta:
        model = Credit
        fields = ("model", "complectation", "first_payment", "duration", "calculator")


class CompareSerializer(serializers.Serializer):
    complectation1 = serializers.CharField(max_length=100)
    complectation2 = serializers.CharField(max_length=100)