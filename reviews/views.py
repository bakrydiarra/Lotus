from django.shortcuts import render,  get_object_or_404, reverse, redirect
from .models import Review
from django.views import generic, View
from django.urls import reverse_lazy


class Reviews(generic.ListView):
    """
    Class to show all the reviews
    """
    model = Review
    queryset = Review.objects.order_by('created_on')
    template_name = 'reviews/reviews.html'


class ThankReview(generic.TemplateView):
    """This view is used to display the thank you Review page"""
    template_name = "reviews/thank_review.html"


class AddReview(CreateView):
    """
    Class to add a Review
    """
    model = Review
    form_class = PersonaForm
    template_name = 'reviews/add_review.html'
    success_url = reverse_lazy('thank_review')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please fill up all fields.')
        return response