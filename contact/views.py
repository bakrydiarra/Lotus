from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


class ContactUs(CreateView):

    """
    class to show a contact form
    """

    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Your message has been sent successfully!')

        # send confirmation email
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = 'Thank you for contacting us'

        # render subject and message templates
        subject = render_to_string(
            "contact/confirmation_emails/confirmation_email_subject.txt",
            {"subject": subject},
        )
        message = form.cleaned_data['message']
        message = render_to_string(
            "contact/confirmation_emails/confirmation_email_body.txt",
            {"name": name, "message": message},
        )

        # send email
        send_mail(
            subject,
            message,
            email,
            [email],
            fail_silently=False,
        )
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please fill up the form completely.')
        return response
