from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
# Create your models here.

class Friend(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_user')
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_user')