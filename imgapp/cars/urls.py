from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('profile/edit-info', views.edit_info, name="edit-info"),
    path('profile/change-password', views.change_password, name="change-password"),
    path('profile/', views.profile_info, name="profile_info"),
    
]