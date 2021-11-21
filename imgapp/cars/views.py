from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.auth import login, authenticate
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
            return redirect("cars: home_view")
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