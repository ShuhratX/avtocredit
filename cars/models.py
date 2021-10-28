from django.db import models
from django.db.models.base import Model
from django.utils import translation

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    complectation = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    power = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    top_speed = models.PositiveIntegerField()