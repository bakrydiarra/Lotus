from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""
    list_display = (
        'name',
        'email',
        'message',
        'reason',
        'written_on',
    )
    list_filter = (
        'name',
        'reason',
        'written_on'
          )


admin.site.register(Contact, ContactAdmin)
