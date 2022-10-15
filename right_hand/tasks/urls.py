from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    # Адреса задач-------------------------------------------------------------
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/', views.task_profile, name='task_profile'),
    path('new/', views.task_new, name='task_new'),
    path('', views.tasks, name='tasks'),

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
    path('interest/new/', views.interest_new, name='interest_new'),
    path('interest/', views.interests, name='interests'),
    # Конец -------------------------------------------------------------------
]
