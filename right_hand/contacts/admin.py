from django.contrib import admin

from .models import Contact, Communication, Company

admin.site.register(Contact)
admin.site.register(Communication)
admin.site.register(Company)
