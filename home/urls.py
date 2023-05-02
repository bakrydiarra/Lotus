from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about_us/', views.AboutUs.as_view(), name='about_us'),
]
