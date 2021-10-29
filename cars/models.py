from django.db import models


class CarModel(models.Model):
    name = models.CharField(max_length=100)


class Complectation(models.Model):
    name = models.CharField(max_length=100)


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    complectation = models.ForeignKey(Complectation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    top_speed = models.PositiveIntegerField()


class Credit(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    complectation = models.ForeignKey(Complectation, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    first_payment = models.CharField(max_length=50)



class Calculator(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name="calculator")
    month = models.DateField()
    payment = models.PositiveIntegerField()
    percent = models.CharField(max_length=20)
    total = models.PositiveIntegerField()
    remains = models.PositiveIntegerField()
