from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Faqs.as_view(), name='faqs'),
    path('add/', views.AddFaq.as_view(), name='add_faq'),
    path(
        'edit_faq/<int:pk>/', views.EditFaq.as_view(), name='edit_faq'
        ),
    path(
        'delete_faq/<int:pk>/', views.DeleteFaq.as_view(), name='delete_faq'
        ),
]
