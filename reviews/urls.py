from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Reviews.as_view(), name='reviews'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('tank_review/', views.ThankReview.as_view(), name='thank_review'),
]
