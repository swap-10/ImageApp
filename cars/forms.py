from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, ReadOnlyPasswordHashWidget, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from django.forms.widgets import SelectDateWidget

from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()

        return user


class EditInfoForm(UserChangeForm):

    password = ReadOnlyPasswordHashField(label=("Password"))
    class Meta:
        model = User
        fields = {
            "password",
            "last_name",
            "first_name",
            "email"
        }


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dob', 'location', 'mobile', 'user_desc', 'interests']
        widgets = {'dob': SelectDateWidget(years=range(1960, 2022))}
    