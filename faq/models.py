from django.db import models
from django.urls import reverse


class Faq(models.Model):
    """Model for FAQ"""

    question = models.CharField(max_length=250, blank=False)
    answer = models.TextField()

    def get_absolute_url(self):
        """Get url after owner adds/edits FAQ"""
        return reverse('faqs')
