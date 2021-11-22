from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm, EditInfoForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successfully signed up")
            return redirect("home")
        messages.error(request, "Unsuccessful signup")
        print(form.errors)
        return HttpResponse(form.errors)
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
                messages.info(request, f"You are now logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid creds")
        else:
            messages.error(request, "Invalid creds structure")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


def logout_view(request, *args, **kwargs):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect("home")

def edit_info(request):
    if (request.method == "POST"):
        form = EditInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/home/profile')
    else:
        if request.user.is_authenticated:
            form = EditInfoForm(instance=request.user)
            args = {'form':form}
            return render(request, "edit-registration.html", args)
        else:
            return redirect("/login")


def change_password(request):
    if (request.method == "POST"):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/home/profile/change-password')
    else:
        if request.user.is_authenticated:
            form = PasswordChangeForm(request.user)
            args = {'form':form}
            return render(request, "change-password.html", args)
        else:
            return redirect('/login')

def profile_info(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect("/login")