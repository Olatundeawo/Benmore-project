from django.urls import path, include
from .views import (task_list, fetch_task, create_task,
 edit_task, delete_task, SearchTask)

urlpatterns = ([
    path('', task_list, name='task_list'),
    path('fetch_task/<str:status>', fetch_task, name='fetch_task'),
    path('create_task/', create_task, name='create_task'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('search/', SearchTask.as_view(), name='search_tasks'),
    
]
)