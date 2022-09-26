from django.shortcuts import redirect, render, get_object_or_404

from .forms import (ContactForm,
                    CommunicationForm,
                    CommunicationFormWithoutContact)
from .models import Communication, Contact


def contacts(request):
    """Все контакты."""
    template = "contacts/contacts.html"
    title = 'Мои контакты.'
    header = title
    contacts = Contact.objects.all()
    context = {
        'title': title,
        'header': header,
        'contacts': contacts,
    }
    return render(request, template, context)


def contacts_profile(request, pk):
    """Страничка конаткта."""
    template = "contacts/contact_profile.html"
    contact = get_object_or_404(Contact, pk=pk)
    title = f'{contact.name}'
    header = title
    context = {
        'title': title,
        'header': header,
        'contact': contact,
    }
    return render(request, template, context)


def contacts_new(request):
    """Добавление нового контакта."""
    form = ContactForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
        return redirect("contacts:contacts")
    template = "contacts/contacts_new.html"
    title = "Новый контакт"
    action = "Добавьте новый контакт"
    context = {
        "title": title,
        "header": title,
        "form": form,
        "action": action,
    }
    return render(request, template, context)


def communications(request):
    """Все комунникации."""
    template = "contacts/communications.html"
    title = 'Мои коммуникации.'
    header = title
    communications = Communication.objects.all()
    context = {
        'title': title,
        'header': header,
        'communications': communications,
    }
    return render(request, template, context)


def communications_new(request):
    """Добавление новой коммуникаци."""
    form = CommunicationForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
        return redirect("contacts:contacts")
    template = "contacts/communications_new.html"
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
        new_communication.contact = Contact.objects.filter(pk=pk)
        form.save(commit=True)
        return redirect("contacts:contact_profile", pk=pk)
    template = "contacts/communications_new_with.html"
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
