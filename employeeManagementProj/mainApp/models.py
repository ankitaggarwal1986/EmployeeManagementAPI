import email
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False)
    email=models.CharField(max_length=200, null=False, blank=False, unique=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    address_details=models.di