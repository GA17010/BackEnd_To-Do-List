from django.urls import path
from . import views

urlpatterns = [
    # List all tasks
    path('tasks/', views.task_list, name='task_list'), 
    # Add a task
    path('tasks/add/', views.task_add, name='task_add'), 
    # Delete a task
    path('tasks/delete/<int:id>/', views.task_delete, name='task_delete'), 
    # Update a task
    path('tasks/update/<int:id>/', views.task_update, name='task_update'), 
]
