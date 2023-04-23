from django import forms
from .models import Contact
from django_summernote.widgets import SummernoteWidget


class ContactForm(forms.ModelForm):
    class Meta:
        # Get a contact form model and choose which fields to display
        model = Contact
        fields = ('reason', 'name', 'email', 'message',)
        # widgets to design input fields

        widgets = {
            'reason': forms.Select(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Give your name here'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Give your email here'
            }),
            'message': SummernoteWidget,
        }
