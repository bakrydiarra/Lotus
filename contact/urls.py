from . import views
from .views import *
from django.urls import path


urlpatterns = [
    path('', ContactUs.as_view(), name='contact')
]
