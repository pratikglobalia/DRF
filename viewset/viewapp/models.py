from unicodedata import name
from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=70)
    mobile = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()