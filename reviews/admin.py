from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """Allows admin to manage reviews via the admin panel"""
    list_display = (
        'name',
        'body',
        'created_on',
        'updated_on'
    )


admin.site.register(Review, ReviewAdmin)
