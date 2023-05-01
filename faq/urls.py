from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Faqs.as_view(), name='faqs'),
]