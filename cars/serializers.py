from django.db.models import fields
from rest_framework import serializers
from .models import *

class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = "___all__"


class ComplectationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complectation
        fields = "___all__"


class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer(required=False, many=False)
    complectation = ComplectationSerializer(required=False, many=False)    
    class Meta:
        model = Car
        fields = "__all__"


class CalculatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculator
        fields = "__all__"


class CreditSerializer(serializers.ModelSerializer):
    calculator = CalculatorSerializer(required=False)    
    class Meta:
        model = Credit
        fields = ("model", "complectation", "first_payment", "duration", "calculator")
