from django.shortcuts import render
from django.views import generic, View


class Home(generic.TemplateView):
    """This view is used to display the home page"""
    template_name = "home/index.html"


class AboutUs(generic.TemplateView):
    """This view is used to display the about us page"""
    template_name = "home/about_us.html"
