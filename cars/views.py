from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EditProfile, SignupForm, EditInfoForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.db import models
from .models import Profile

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user.pk)
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return render(request, "welcome.html")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
        return render(request=request, template_name="signup.html", context={"signup_form":form})
    form = SignupForm()
    return render(request=request, template_name="signup.html", context={"signup_form":form})


def login_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
        else:
            return render(request, "login.html", {"login_form":form})
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form":form})


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect(reverse("home"))

def edit_info(request):
    if (request.method == "POST"):
        form = EditInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse("profile"))
    else:
        if request.user.is_authenticated:
            form = EditInfoForm(instance=request.user)
            args = {'form':form}
            return render(request, "edit-registration.html", args)
        else:
            return redirect(reverse("login"))


def change_password(request):
    if (request.method == "POST"):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse("change-password"))
    else:
        if request.user.is_authenticated:
            form = PasswordChangeForm(request.user)
            args = {'form':form}
            return render(request, "change-password.html", args)
        else:
            return redirect(reverse("login"))

def profile_info(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect(reverse("login"))

def edit_profile(request, *args, **kwargs):
    if request.user.is_authenticated:
        if (request.method == "POST"):

            if Profile.objects.filter(pk=request.user.pk).exists():
                instance = Profile.objects.get(pk=request.user.pk)
                form = EditProfile(request.POST, instance=instance)
                form.fields['dob'].disabled = True
                if form.is_valid():
                    form.save()
                    return redirect(reverse("profile"))
                else:
                    form.fields['dob'].disabled = True
                    return render(request, "edit-profile.html", {"form":form})
                
            else:
                form = EditProfile(request.POST)
                if form.is_valid():
                    profile = form.save(commit=False)
                    profile.user = request.user
                    profile.save()
                    return redirect(reverse("profile"))
                else:
                    return render(request, "edit-profile.html", {"form":form})
        
        else:
            if Profile.objects.filter(pk=request.user.pk).exists():
                instance = Profile.objects.get(pk=request.user.pk)
                form = EditProfile(instance=instance)
                form.fields['dob'].disabled = True
                args = {'form':form}
                return render(request, "edit-profile.html", args)
            else:
                form = EditProfile()
                args = {'form':form}
                return render(request, "edit-profile.html", args)
    else:
        return redirect(reverse("login"))    
