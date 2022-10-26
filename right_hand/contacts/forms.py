from django import forms

from .models import Contact, Communication, Company


class ContactForm(forms.ModelForm):
    """Форма для создания контакта."""
    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "phone_number",
            "role",
            "date_of_birthday",
            "frequency_of_communications_days",
            "company",
        )


class ContactFormWithPartner(forms.ModelForm):
    """Форма для создания сотрудника компании."""
    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "date_of_birthday",
            "frequency_of_communications_days",
        )


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = (
            'type',
            'contact',
            'info',
        )


class CommunicationFormWithoutContact(forms.ModelForm):
    class Meta:
        model = Communication
        fields = (
            'type',
            'info',
        )


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            "inn",
            "kpp",
            "ogrn",
            "okpo",
            "okved",
            "fact_adress",
            "legal_adress",
            "full_name",
            "short_name",
            "main_email",
            "phone_number",
            "number_acount",
            "cor_acount",
            "bic",
            "head_of_company",
        )
