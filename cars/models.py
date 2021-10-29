from django.db import models
from django.db.models.base import Model
from django.utils import translation


class CarModel(models.Model):
    name = models.CharField(max_length=100)


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    complectation = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    top_speed = models.PositiveIntegerField()


class Credit(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    percent = models.PositiveIntegerField()
    first_payment = models.CharField(max_length=50)


class Calculator(models.Model):
    month = models.DateField()
    payment = models.PositiveIntegerField()
    percent = models.CharField(max_length=20)
    total = models.PositiveIntegerField()
    remains = models.PositiveIntegerField()
