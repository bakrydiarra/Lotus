from django.contrib import admin
from .models import Review
from product.models import Category


class ReviewAdmin(admin.ModelAdmin):
    """Allows admin to manage Testimonials via the admin panel"""
    list_display = (
        'name',
        'category',
        'created_on',
        'updated_on'
    )


admin.site.register(Review, ReviewAdmin)
