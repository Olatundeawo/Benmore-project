from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, TaskFilterForm
from django.views import View
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    progress = Task.objects.filter(status='progress')
    completed = Task.objects.filter(status='completed')
    overdue = Task.objects.filter(status='overdue')
    query = request.GET.get('q', '')
    if query:

        tasks = Task.objects.filter(Q(description__icontains=query) | Q(title__icontains=query))
        tasks_data = list(tasks.values('id', 'title', 'description', 'status', 'priority', 'due_date'))
        
    else:
        tasks_data = []
    
    
    context = {
        'progress': progress,
        'progress_count': progress.count(),
        'overdue': overdue,
        'overdue_count': overdue.count(),
        'completed': completed,
        'completed_count': completed.count(),
        'tasks_data': tasks_data,
        # 'search_progress': search_progress,
        # 'search_completed': search_completed,
        # 'search_overdue': search_overdue,
        'query': query,
    }
    return (render(request,'task_list.html', context))


def fetch_task(request, status):
    tasks = Task.objects.filter(status=status)
    return (render(request, 'fetch_task.html', {'tasks':tasks}))


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return (redirect('task_list'))
    else:
        form = TaskForm()
       
    return (render(request, 'create_task.html', {'form':form}))


def filter_tasks(request):
    form = TaskFilterForm(request.GET)
    tasks = Task.objects.all()
    if form.is_valid():
        query = form.cleaned_data.get('q')
        priority = form.cleaned_data.get('priority')
        due_date = form.cleaned_data.get('due_date')
        category = form.cleaned_data.get('category')

        filters = Q()
        if query:
            filters &= Q(description__icontains=query) | Q(title__icontains=query)
        if priority:
            filters &= Q(priority=priority)
        if due_date:
            filters &= Q(due_date=due_date)
        if category:
            filters &= Q(category__icontains=category)  # Assuming category is a CharField

        tasks = Task.objects.filter(filters)

    # tasks_data = list(tasks.values('id', 'title', 'description', 'status', 'priority', 'due_date', 'category'))
    return(render(request, 'filter_tasks.html', {'form': form}))


def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return(redirect('task_list'))
    else:
        form = TaskForm(instance=task)
    return(render(request,'edit_task.html', {'form':form}))

def delete_task(request, id):
    task = Task.objects.get(pk = id)
    task.delete()
    return(redirect('task_list'))
    
    
class SearchTask(View):
   def get(self, request):
        query = request.GET.get('q', '')
        tasks = Task.objects.filter(Q(description__icontains=query) | Q(title__icontains=query))
        tasks_data = list(tasks.values('id', 'title', 'description', 'status', 'priority', 'due_date'))
        return (render(request, 'search_task.html', {'tasks': tasks_data}))