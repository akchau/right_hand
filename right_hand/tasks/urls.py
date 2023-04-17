from django.urls import path

from . import views
from tasks import views as task_views

app_name = 'tasks'

urlpatterns = [
    # Адреса задач ------------------------------------------------------------
    path('', views.tasks, name='tasks'),
    path('<int:pk>/', views.task, name='task'),
    path('new/', views.new, name='new'),
    # Кнопки управления -------------------------------------------------------
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/subtask/', views.subtask, name='subtask'),
    path('<int:pk>/done/', views.done, name='done'),
    path('<int:pk>/in_work/', views.in_work, name='in_work'),
    path('<int:pk>/stop/', views.stop, name='stop'),
    path('<int:pk>/cancel/', views.cancel, name='cancel'),
    # Адреса проектов ---------------------------------------------------------
    path(
        'project/<int:pk>/delete/',
        views.project_delete,
        name='project_delete'
    ),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('project/<int:pk>/', views.project_profile, name='project_profile'),
    path('project/new/', views.project_new, name='project_new'),
    path('projects/', views.projects, name='projects'),
    path(
        'project/new_communication/<int:pk>/',
        views.new_communicaitions_of_project,
        name='project_communication_new'
    ),
    # Адреса интересов --------------------------------------------------------
    path(
        'interest/<int:pk>/delete/',
        views.interest_delete,
        name='interest_delete'
    ),
    path('interest/<int:pk>/edit/', views.interest_edit, name='interest_edit'),
    path(
        'interest/<int:pk>/',
        views.interest_profile,
        name='interest_profile'
    ),
    path(
        'interest/new_with/<int:pk>/',
        views.interest_new_with_partner,
        name='interest_new_with_partner'
    ),
    path('interest/new/', views.interest_new, name='interest_new'),
    path(
        'interest/new_communication/<int:pk>/',
        views.new_communicaitions_of_interest,
        name='interest_communication_new'
    ),
    path('interest/', views.interests, name='interests'),
    # Конец -------------------------------------------------------------------
]
