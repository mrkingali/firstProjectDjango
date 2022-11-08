from django.db import models

# Create your models here.

class User(models.Model):
    id1=models.BigIntegerField()
    name=models.CharField(max_length=100,unique=True)
    dateOfBirth=models.DateField()


class Product(models.Model):
    id1=models.BigIntegerField()
    name=models.CharField(max_length=100)
    productId=models.CharField(max_length=15)
