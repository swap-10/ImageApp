from django.contrib import admin
from django.urls import path, reverse
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.add_friend, name='friends'),
    path('add/', views.add_friend, name='add_friend'),
    path('<str:username>/images/', views.friend_imgs, name='friend_images'),
]