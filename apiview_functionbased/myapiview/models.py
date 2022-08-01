from unicodedata import name
from django.db import models

# Create your models here.
post_choice = (('senior','senior'),('junior','junior'))
class Employee(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    post = models.CharField(max_length=70, choices=post_choice)
    salary =models.IntegerField()