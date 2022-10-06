from datetime import datetime, timedelta

from django.shortcuts import redirect, render, get_object_or_404

from .forms import (ContactForm,
                    ContactFormWithPartner,
                    CommunicationForm,
                    CommunicationFormWithoutContact,
                    PartnerForm)
from .models import Communication, Company, Contact


def contacts(request):
    """Все контакты."""
    template = "contacts/contacts.html"
    title = 'Мои контакты.'
    header = title
    contacts = Contact.objects.all().order_by(
        "frequency_of_communications_days")
    context = {
        'title': title,
        'header': header,
        'contacts': contacts,
    }
    return render(request, template, context)


def contact_profile(request, pk):
    """Страничка конаткта."""
    template = "contacts/contact_profile.html"
    contact = get_object_or_404(Contact, pk=pk)
    communications = Communication.objects.filter(
        contact=contact).order_by('-pub_date')
    title = f'{contact.name}'
    header = title
    context = {
        'title': title,
        'header': header,
        'contact': contact,
        'communications': communications,
    }
    return render(request, template, context)


def contact_new(request):
    """Добавление нового контакта."""
    form = ContactForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
        return redirect("contacts:contacts")
    template = "contacts/contact_new.html"
    title = "Новый контакт"
    action = "Добавьте новый контакт"
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def contact_new_with_partner(request, pk):
    """Добавление нового контакта."""
    form = ContactFormWithPartner(
        request.POST or None,
    )
    if form.is_valid():
        new_contact = form.save(commit=False)
        new_contact.company = Company.objects.get(pk=pk)
        new_contact.role = 'Деловой партнер'
        form.save(commit=True)
        return redirect("contacts:partner_profile", pk=pk)
    template = "contacts/contact_new.html"
    title = "Новый контакт компании."
    action = "Добавьте новый контакт партнера."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
        "with_patrner": True,
        "pk": pk,
    }
    return render(request, template, context)


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(
        request.POST or None,
        files=request.FILES or None,
        instance=contact,
    )
    if form.is_valid():
        form.save()
        return redirect("contacts:contact_profile", pk=pk)
    title = "Редактирование контакта"
    header = title
    action = "Редактируйте контакт"
    template = "contacts/contact_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)


def contact_delete(request, pk):
    Contact.objects.get(pk=pk).delete()
    return redirect("contacts:contacts")


def communications(request):
    """Все комунникации."""
    template = "contacts/communications.html"
    title = 'Мои коммуникации.'
    header = title
    plan_communication = Communication.objects.filter(
        status='Запланировано').order_by('-pub_date')
    communications = Communication.objects.filter(
        status='Выполнена').order_by('-pub_date')
    context = {
        'title': title,
        'header': header,
        'plan_communication': plan_communication,
        'communications': communications,
    }
    return render(request, template, context)


def communications_new(request):
    """Добавление новой коммуникаци."""
    form = CommunicationForm(
        request.POST or None,
    )
    if form.is_valid():
        new_communication = form.save(commit=False)
        new_communication.status = "Выполнен"
        form.save(commit=True)
        return redirect("contacts:communications")
    template = "contacts/communication_new.html"
    title = "Новая коммуникация."
    action = "Добавьте новую коммуникацию."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def communications_new_with_contact(request, pk):
    """Добавление новой коммуникаци."""
    form = CommunicationFormWithoutContact(
        request.POST or None,
    )
    if form.is_valid():
        new_communication = form.save(commit=False)
        new_communication.contact = Contact.objects.get(pk=pk)
        new_communication.status = "Выполнен"
        form.save(commit=True)
        future_communication = Communication(
            type='Переписка',
            status='Запланировано',
            contact=new_communication.contact,
            plan_date=datetime.today() + timedelta(
                days=new_communication.contact.frequency_of_communications_days
            )
        )
        future_communication.save()
        return redirect("contacts:contact_profile", pk=pk)
    template = "contacts/communication_new_with.html"
    title = "Новая коммуникация c контактом."
    action = "Добавьте новую коммуникацию c контактом."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
        "pk": pk,
    }
    return render(request, template, context)


def communication_profile(request, pk):
    """Страничка конаткта."""
    template = "contacts/communication_profile.html"
    communication = get_object_or_404(Communication, pk=pk)
    title = f'{communication}'
    header = title
    context = {
        'title': title,
        'header': header,
        'communication': communication,
    }
    return render(request, template, context)


def communication_edit(request, pk):
    communication = get_object_or_404(Communication, pk=pk)
    form = CommunicationForm(
        request.POST or None,
        files=request.FILES or None,
        instance=communication,
    )
    if form.is_valid():
        form.save()
        return redirect("contacts:communications")
    title = "Редактирование коммуникации."
    header = title
    action = "Редактируйте коммуникацию."
    template = "contacts/communication_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)


def partners(request):
    """Все компании."""
    template = "contacts/partners.html"
    title = 'Все компании.'
    header = title
    companies = Company.objects.all()
    context = {
        'title': title,
        'header': header,
        'companies': companies,
    }
    return render(request, template, context)


def partner_profile(request, pk):
    """Профиль компании."""
    template = "contacts/partner_profile.html"
    company = get_object_or_404(Company, pk=pk)
    title = 'Профиль компании.'
    header = title
    context = {
        'title': title,
        'header': header,
        'company': company,
    }
    return render(request, template, context)


def partner_new(request):
    """Добавление новой компании."""
    form = PartnerForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
        return redirect("contacts:partners")
    template = "contacts/partner_new.html"
    title = "Новая компания."
    action = "Добавьте новую компанию."
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def partner_delete(request, pk):
    Company.objects.get(pk=pk).delete()
    return redirect("contacts:partners")


def communication_delete(request, pk):
    Communication.objects.get(pk=pk).delete()
    return redirect("contacts:communications")


def partner_edit(request, pk):
    partner = get_object_or_404(Company, pk=pk)
    form = PartnerForm(
        request.POST or None,
        files=request.FILES or None,
        instance=partner,
    )
    if form.is_valid():
        form.save()
        return redirect("contacts:partner_profile", pk=pk)
    title = "Редактирование компании."
    header = title
    action = "Редактируйте данные компании."
    template = "contacts/partner_new.html"
    context = {
        "title": title,
        "header": header,
        "action": action,
        "form": form,
        "is_edit": True,
        "pk": pk,
    }
    return render(request, template, context)
