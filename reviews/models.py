from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Review(models.Model):
    """Model for Review"""
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews")
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ To sort comments in ascending oder """
        ordering = ['created_on']

    def get_absolute_url(self):
        """Get url after user adds/edits review"""
        return reverse('reviews')

    def __str__(self):
        return f"Review: {self.category} by {self.name}"
