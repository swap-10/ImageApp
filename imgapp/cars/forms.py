from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1960, 2022)))
    fullname = forms.CharField(required=True)
    location = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "fullname", "location", "mobile", "dob", "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.dob = self.cleaned_data['dob']
        user.fullname = self.cleaned_data['fullname']
        user.location = self.cleaned_data['location']
        user.mobile = self.cleaned_data['mobile']
        if commit:
            user.save()

        return user