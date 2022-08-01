from django.db import models

# Create your models here.
gender_choices = (('M','male'),('F','female'))
class Person(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    gender = models.CharField(max_length=1, choices=gender_choices)
    age = models.IntegerField()
    qualification = models.CharField(max_length=100)

    
    
    
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwars):
    if created:
        Token.objects.create(user=instance)