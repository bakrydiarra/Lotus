from django.shortcuts import render,  get_object_or_404, reverse, redirect
from .models import Review
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
    form_class = ReviewForm
    template_name = 'reviews/add_review.html'
    success_url = reverse_lazy('thank_review')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please fill up all fields.')
        return response


class EditReview(LoginRequiredMixin, UpdateView):

    """
    Class to edit review
    """

    model = Review
    form_class = ReviewForm
    template_name = 'reviews/edit_review.html'
    success_url = reverse_lazy('thank_review')

    """
    to get the original queryset of all Review objects
    to filter onlyto include objects where the user
    matches the currently logged in user
    """

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(name=self.request.user)
        return queryset

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please fill up all fields.')
        return

    def dispatch(self, request, *args, **kwargs):
        """
        check that the current user
        is the owner of the review
        """
        if self.get_object().name != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class DeleteReview(LoginRequiredMixin, DeleteView):
    """
    Class to delete a Review
    """
    model = Review
    template_name = 'reviews/delete_review.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """
        check that the current user
        is the owner of the review
        """
        if self.get_object().name != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
