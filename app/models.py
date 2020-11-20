from django.db import models


class Auction(models.Model):
    product = models.CharField(max_length=50)
    count = models.IntegerField()
    cost = models.FloatField()
    username = models.CharField(max_length=50)
    date = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    cost = models.FloatField()
    farm = models.CharField(max_length=50)


class Farm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10)
    name_directors = models.CharField(max_length=150)
    phone_directors = models.CharField(max_length=10)


# Create your models here.
