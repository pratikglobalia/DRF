from django.db import models

# Create your models here.
class Mobile(models.Model):
    mobile = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()