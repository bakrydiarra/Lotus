from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Reviews.as_view(), name='reviews'),
    path('add/', views.AddReview.as_view(), name='add_review'),
    path('thank_review/', views.ThankReview.as_view(), name='thank_review'),
    path(
        'edit_review/<int:pk>/', views.EditReview.as_view(), name='edit_review'
        ),
    path(
        'delete_review/<int:pk>/', views.DeleteReview.as_view(),
        name='delete_review'
        ),
]
