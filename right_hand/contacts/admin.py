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
        'is_expired',
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


class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'inn',
        'kpp',
        'ogrn',
        'okpo',
        'okved',
        'fact_adress',
        'legal_adress',
        'full_name',
        'short_name',
        'main_email',
        'number_acount',
        'cor_acount',
        'bic',
        'head_of_company',
        "mobile_number_of_head",
    )
    list_editable = (
        'inn',
        'kpp',
        'ogrn',
        'okpo',
        'okved',
        'fact_adress',
        'legal_adress',
        'full_name',
        'short_name',
        'main_email',
        'number_acount',
        'cor_acount',
        'bic',
        'head_of_company',
        "mobile_number_of_head"
    )
    search_fields = (
        'inn',
        'kpp',
        'ogrn',
        'okpo',
        'okved',
        'fact_adress',
        'legal_adress',
        'full_name',
        'short_name',
        'phone_number',
        'number_acount',
        'cor_acount',
        'bic',
        'head_of_company'
    )
    list_filter = ('short_name',)
    empty_value_display = "-пусто-"


admin.site.register(Contact, ContactAdmin)
admin.site.register(Communication, CommunicationAdmin)
admin.site.register(Company, PartnerAdmin)
