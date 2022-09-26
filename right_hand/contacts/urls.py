from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path(
        'contacts/<int:pk>/',
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
]
