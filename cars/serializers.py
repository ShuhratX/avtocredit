from django.db.models import fields
from rest_framework import serializers
from .models import *

class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = "___all__"


class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer(required=False, many=False)    
    class Meta:
        model = Car
        fields = "__all__"


class Credit(serializers.ModelSerializer):
    
    class Meta:
        model = Credit
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = "__all__"