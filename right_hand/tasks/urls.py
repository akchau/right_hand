from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('<int:pk>/', views.task_profile, name='task_profile'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('new/', views.task_new, name='task_new'),
    path('', views.tasks, name='tasks'),


    path('project/<int:pk>/', views.project_profile, name='project_profile'),
    path(
        'project/<int:pk>/delete/',
        views.project_delete,
        name='project_delete'
    ),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('project/new/', views.project_new, name='project_new'),
    path('projects/', views.projects, name='projects'),

]
