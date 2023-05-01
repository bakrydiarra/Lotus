from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Faq(models.Model):
    """Model for FAQ"""

    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="faqs")
    question = models.CharField(max_length=250, blank=False)
    answer = models.TextField()

    def get_absolute_url(self):
        """Get url after owner adds/edits FAQ"""
        return reverse('faqs')
