from django.urls import path, include

from . import views

app_name = 'contacts'

urlpatterns = [
    path(
        'debug_api/',
        include('contacts.api.urls')
    ),
    path('', views.contacts, name='contacts'),
    path(
        '<int:pk>/',
        views.contact_profile,
        name='contact_profile'
    ),
    path('new/', views.contact_new, name='contact_new'),
    path(
        'new_with_partner/<int:pk>/',
        views.contact_new_with_partner,
        name='contact_new_with_partner'
    ),
    path(
        '<int:pk>/edit/',
        views.contact_edit,
        name='contact_edit'
    ),
    path(
        '<int:pk>/delete/',
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
        'communication/new_with/<int:pk>/',
        views.communications_new_with_contact,
        name='communication_new_with_contact'
    ),
    path(
        'communication/<int:pk>/',
        views.communication_profile,
        name='communication_profile'
    ),
    path(
        'communication/<int:pk>/edit/',
        views.communication_edit,
        name='communication_edit'
    ),
    path(
        'communications/<int:pk>/delete/',
        views.communication_delete,
        name='communication_delete'
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
        'partner/<int:pk>/requsites/',
        views.partner_requisites,
        name='partner_requisites'
    ),

    path(
        'partner/new/',
        views.partner_new,
        name='partner_new'
    ),
    path(
        'partner/<int:pk>/delete/',
        views.partner_delete,
        name='partner_delete'
    ),
    path(
        'partner/<int:pk>/edit/',
        views.partner_edit,
        name='partner_edit'
    ),
    path(
        'communication/<int:pk>/done/',
        views.communication_complete,
        name='communication_complete'
    ),
]
