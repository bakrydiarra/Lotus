from django.shortcuts import render
from .models import Faq
from django.views import generic, View


class Faqs(generic.ListView):
    """
    Class to show all the Faqs
    """
    model = Faq
    template_name = 'faq/faqs.html'
