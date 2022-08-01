from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    auther = models.CharField(max_length=70)
    price = models.IntegerField()
    publish_date = models.DateField()