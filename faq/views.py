from django.shortcuts import render
from .models import Faq
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import FaqForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Faqs(generic.ListView):
    """
    Class to show all the Faqs
    """
    model = Faq
    template_name = 'faqs/faqs.html'


class AddFaq(CreateView):
    """
    Class to add a Faq
    """
    model = Faq
    form_class = FaqForm
    template_name = 'faqs/add_faq.html'
    success_url = reverse_lazy('faqs')

    def form_valid(self, form):
        form.instance.name = self.request.user
        self.request.user == self.request.user.is_superuser
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please fill up all fields.')
        return response


class EditFaq(LoginRequiredMixin, UpdateView):

    """
    Class to edit faq
    """

    model = Faq
    form_class = FaqForm
    template_name = 'faqs/edit_faq.html'
    success_url = reverse_lazy('faqs')

    def form_valid(self, form):
        form.instance.name = self.request.user
        self.request.user == self.request.user.is_superuser
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please fill up all fields.')
        return

    def dispatch(self, request, *args, **kwargs):
        """
        check that the current user
        is the owner of the faq
        """
        if self.get_object().name != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)