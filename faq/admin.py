from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    """Allows admin to manage FAQs via the admin panel"""
    list_display = (
        'question',
        'amswer',
    )


admin.site.register(Faq, FaqAdmin)
