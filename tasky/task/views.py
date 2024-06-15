from django.shortcuts import render
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.object.all()
    return (render(request,'template/task_list.html', {'tasks': tasks}))


def fetch_task(request, status):
    tasks = Task.object.filter(status=status)
    return (render(request, 'template/fetch_card.html', {'tasks':tasks}))
