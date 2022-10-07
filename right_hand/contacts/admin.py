from django.contrib import admin

from .models import Contact, Communication, Company


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'role',
        'email',
        'frequency_of_communications_days',
        'date_of_birthday',
        'company',
        'position',
    )
    list_editable = (
        'name',
        'role',
        'email',
        'frequency_of_communications_days',
        'date_of_birthday',
        'company',
        'position',
    )
    search_fields = ("name", "role", "position")
    list_filter = ('frequency_of_communications_days',)
    empty_value_display = "-пусто-"


class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'type',
        'status',
        'contact',
        'pub_date',
        'plan_date',
        'info',
    )
    list_editable = (
        'type',
        'status',
        'contact',
        'plan_date',
        'info',
    )
    search_fields = ("type", "status", "info")
    list_filter = ('pub_date',)
    empty_value_display = "-пусто-"


admin.site.register(Contact, ContactAdmin)
admin.site.register(Communication, CommunicationAdmin)
admin.site.register(Company)
