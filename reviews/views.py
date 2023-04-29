from django.shortcuts import render,  get_object_or_404, reverse, redirect
from .models import Review
from django.views import generic, View


class Reviews(generic.ListView):
    """
    Class to show all the reviews
    """
    model = Review
    queryset = Review.objects.order_by('created_on')
    template_name = 'reviews/reviews.html'
