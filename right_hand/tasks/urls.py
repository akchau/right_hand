from django.urls import path

from . import views
from tasks import views as task_views

app_name = 'tasks'

urlpatterns = [
    # Адреса задач-------------------------------------------------------------
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/', views.task_profile, name='task_profile'),
    path(
        'new_with_project/<int:pk>/',
        task_views.task_new_with_project,
        name='task_new_with_project'
    ),
    path('new/', views.task_new, name='task_new'),
    path('<int:pk>/done/', views.task_done, name='task_done'),
    path('', views.tasks, name='tasks'),
    # Адреса категорий задач---------------------------------------------------
    path('category/<int:pk>/delete/',
         views.category_of_task_delete,
         name='category_of_task_delete'),
    path('category/<int:pk>/edit/',
         views.category_of_task_edit,
         name='category_of_task_edit'),
    path('category/<int:pk>/',
         views.category_of_task_profile,
         name='category_of_task_profile'),
    path('category/new/',
         views.category_of_task_new,
         name='category_of_task_new'),
    path('category/',
         views.categories_of_tasks,
         name='categories_of_tasks'),
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
