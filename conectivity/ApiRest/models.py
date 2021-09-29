from django.db import models

# Create your models here.

class People(models.Model):
    cod = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    height = models.CharField(max_length=100, blank=False, null=False)

# class PrimeNumber(models.Model):
#     cod = models.AutoField(primary_key=True)