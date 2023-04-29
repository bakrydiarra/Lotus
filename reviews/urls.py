from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Reviews.as_view(), name='reviews'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('thank_review/', views.ThankReview.as_view(), name='thank_review'),
    path(
        'edit_review/<int:pk>/', EditReviewView.as_view(), name='edit_review'
        ),
    path(
        'delete_review/<int:pk>/', DeleteReviewView.as_view(),
        name='delete_review'
        ),
]
