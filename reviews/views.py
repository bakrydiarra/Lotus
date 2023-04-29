from django.shortcuts import render,  get_object_or_404, reverse, redirect
from .models import Review
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ReviewForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


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


@login_required
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


@login_required
class EditReview(UpdateView):

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


@login_required
class DeleteReview(DeleteView):
    """
    Class to delete a Review
    """
    model = Review
    template_name = 'reviews/delete_review.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        """
        Prevent a review to be deleted by user
        who hasn't written it
        """
        review = self.get_object()
        if review.created_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
