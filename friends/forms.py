from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Friend

class FriendForm(ModelForm):
    friend_id = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Friend
        exclude = ['user']

