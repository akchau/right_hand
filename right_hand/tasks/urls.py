from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('task/<int:pk>/', views.task_profile, name='task_profile'),
]
