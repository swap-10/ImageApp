"""imgapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from cars import views as cars_views
from django.conf import settings
from django.conf.urls.static import static
import cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cars_views.home_view, name="home"),
    path('home/', cars_views.home_view, name="homeexact"),
    path('account/', include('cars.urls')),
    path('images/', include('imgs.urls')),
    path('friends/', include('friends.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
