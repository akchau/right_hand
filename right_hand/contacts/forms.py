from django import forms

from .models import Contact, Communication


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "is_family",
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
