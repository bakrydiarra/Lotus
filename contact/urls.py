from . import views
from .views import *
from django.urls import path


urlpatterns = [
    path('', ContactUs.as_view(), name='contact'),
    path('received_msg/', views.ReceivedMsg.as_view(), name='received_msg'),
]
