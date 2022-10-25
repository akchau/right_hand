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

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        data = data.strip()
        elements = [
            '+',
            '-',
            ' ',
            ')',
            '(',
        ]
        numbers_all = [str(x) for x in range(10)]
        for element in elements:
            data = data.replace(element, '')
        for sign in data:
            if sign not in numbers_all:
                raise forms.ValidationError('Неверные символы')
        len_number = len(data)
        if len_number < 10 or len_number > 11:
            raise forms.ValidationError('Неверная длинна номера')
        if len_number == 10:
            data = f'7{data}'
        data = (f'+7({data[1:4]})-'
                f'{data[4:7]}-'
                f'{data[7:9]}-{data[9:11]}')
        return data


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

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        data = data.strip()
        elements = [
            '+',
            '-',
            ' ',
            ')',
            '(',
        ]
        numbers_all = [str(x) for x in range(10)]
        for element in elements:
            data = data.replace(element, '')
        for sign in data:
            if sign not in numbers_all:
                raise forms.ValidationError('Неверные символы')
        len_number = len(data)
        if len_number < 10 or len_number > 11:
            raise forms.ValidationError('Неверная длинна номера')
        if len_number == 10:
            data = f'7{data}'
        data = (f'+7({data[1:4]})-'
                f'{data[4:7]}-'
                f'{data[7:9]}-{data[9:11]}')
        return data
