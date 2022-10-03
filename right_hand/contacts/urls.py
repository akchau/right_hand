from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path(
        'contact/<int:pk>/',
        views.contacts_profile,
        name='contacts_profile'
    ),
    path('contacts/new/', views.contacts_new, name='contacts_new'),
    path('communications/', views.communications, name='communications'),
    path(
        'communications_new/',
        views.communications_new,
        name='communications_new'
    ),
    path(
        'communications_new_with/<int:pk>/',
        views.communications_new_with_contact,
        name='communications_new_with_contact'
    ),
    path(
        'partners/',
        views.partners,
        name='partners'
    ),
    path(
        'partners/<int:pk>/',
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
        'contacts/<int:pk>/delete/',
        views.contact_delete,
        name='contact_delete'
    ),
    path(
        'communications/<int:pk>/delete/',
        views.communication_delete,
        name='communication_delete'
    ),
    path(
        'contact/<int:pk>/edit/',
        views.contact_edit,
        name='contact_edit'
    ),
]
