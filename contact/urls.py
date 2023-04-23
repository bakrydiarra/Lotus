from . import views
from django.urls import path


urlpatterns = [
    path('', ContactUs.as_view(), name='contact')
]
