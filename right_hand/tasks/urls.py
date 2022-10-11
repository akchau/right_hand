from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('task/<int:pk>/', views.task_profile, name='task_profile'),
    path('task/<int:pk>/delete/', views.task_delete name='task_delete'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
]
