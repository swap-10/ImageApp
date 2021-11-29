from django.contrib import admin
from django.urls import path, reverse
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('upload/', views.upload, name="upload"),
]