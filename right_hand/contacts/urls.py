from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path(
        'contact/<int:pk>/',
        views.contact_profile,
        name='contact_profile'
    ),
    path('contact/new/', views.contact_new, name='contact_new'),
    path(
        'contact/new/with_partner/<int:pk>/',
        views.contact_new_with_partner,
        name='contact_new_with_partner'
    ),
    path(
        'contact/<int:pk>/edit/',
        views.contact_edit,
        name='contact_edit'
    ),
    path(
        'contact/<int:pk>/delete/',
        views.contact_delete,
        name='contact_delete'
    ),
    path('communications/', views.communications, name='communications'),
    path(
        'communication/new/',
        views.communications_new,
        name='communication_new'
    ),
    path(
        'communication_new_with/<int:pk>/',
        views.communications_new_with_contact,
        name='communication_new_with_contact'
    ),
    path(
        'partners/',
        views.partners,
        name='partners'
    ),
    path(
        'partner/<int:pk>/',
        views.partner_profile,
        name='partner_profile'
    ),

    path(
        'partners/new/',
        views.partner_new,
        name='partner_new'
    ),
    path(
        'partners/<int:pk>/delete/',
        views.partner_delete,
        name='partner_delete'
    ),
    path(
        'communications/<int:pk>/delete/',
        views.communication_delete,
        name='communication_delete'
    ),
    path(
        'partner/<int:pk>/edit/',
        views.partner_edit,
        name='partner_edit'
    ),
    path(
        'communication/<int:pk>/edit/',
        views.communication_edit,
        name='communication_edit'
    ),
]
