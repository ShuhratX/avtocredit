from django.db import models
import datetime


class CarModel(models.Model):
    title = models.CharField(max_length=100)


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="models")
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    top_speed = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Credit(models.Model):
    CHOICE = (
        ('credit', ('Credit')),
        ('leasing', ('Leasing')),
    )
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="credit")
    title = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="credit")
    month = models.PositiveIntegerField(default=12)
    status = models.CharField(choices=CHOICE, max_length=50)

    def __str__(self):
        return self.model.title


class Calculator(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name="payments")
    sum = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=1)
    percent = models.CharField(max_length=20)
    total = models.PositiveIntegerField()
    remain = models.PositiveIntegerField()
