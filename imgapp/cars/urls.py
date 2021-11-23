from django.contrib import admin
from django.urls import path, reverse
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_info, name="profile"),
    path('profile/edit-info', views.edit_info, name="edit-info"),
    path('profile/change-password', views.change_password, name="change-password"),
    path('profile/edit-profile', views.edit_profile, name="edit-profile"),
    
]