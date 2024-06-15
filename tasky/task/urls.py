from django.urls import path, include
from .views import task_list, fetch_task

urlpatterns = ([
    path('', task_list, name='task_list'),
    path('fetch_tasks/<str:status>', fetch_task, name='fecth_task'),
]
)