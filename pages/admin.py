from django.contrib import admin
from pages.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'message']


admin.site.register(Contact, ContactAdmin)
