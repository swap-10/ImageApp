from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from iso3166 import countries
# Create your models here.

class Profile(models.Model):
    COUNTRY_CHOICES = [(c.alpha2, c.name) for c in countries]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateField()
    location = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    mobile = models.CharField(max_length=15)
    user_desc = models.CharField(max_length=200, blank=True, null=True)
    interests = models.CharField(max_length=200, blank=True, null=True)


