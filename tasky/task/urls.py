from django.urls import path, include
from .views import (
    task_list, fetch_task, create_task, 
    edit_task, delete_task, SearchTask
)

# Define the URL patterns for the task management app
urlpatterns = [
    # URL pattern for the task list view
    path('', task_list, name='task_list'),
    
    # URL pattern for fetching tasks based on their status via AJAX
    path('fetch_task/<str:status>', fetch_task, name='fetch_task'),
    
    # URL pattern for creating a new task
    path('create_task/', create_task, name='create_task'),
    
    # URL pattern for editing an existing task
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    
    # URL pattern for deleting a task
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    
    # URL pattern for searching tasks
    path('search/', SearchTask.as_view(), name='search_tasks'),
]
