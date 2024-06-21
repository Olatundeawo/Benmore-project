from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, TaskFilterForm
from django.views import View
from django.db.models import Q
from django.http import JsonResponse

# View to display the list of tasks
def task_list(request):
    """
    Display a list of tasks, filtered by various criteria such as search query, category, due date, and priority.
    """
    # Retrieve all tasks
    tasks = Task.objects.all()
    
    # Retrieve tasks based on status
    progress = Task.objects.filter(status='progress')
    completed = Task.objects.filter(status='completed')
    overdue = Task.objects.filter(status='overdue')

    # Get filter parameters from the request
    query = request.GET.get('q', '')  # Search query
    
    # Filter tasks by search query if provided
    if query:
        tasks = Task.objects.filter(Q(description__icontains=query) | Q(title__icontains=query))
        tasks_data = list(tasks.values('id', 'title', 'description', 'category', 'status', 'priority', 'due_date'))
    else:
        tasks_data = []

    

    # Prepare context data for the template
    context = {
        'progress': progress,
        'progress_count': progress.count(),
        'overdue': overdue,
        'overdue_count': overdue.count(),
        'completed': completed,
        'completed_count': completed.count(),
        'query': query,
        'tasks': tasks,
    }

    # Render the task list template with the context data
    return render(request, 'task_list.html', context)


# View to fetch tasks based on status via AJAX
def fetch_task(request, status):
    """
    Fetch tasks based on their status and return a partial template for AJAX requests.
    """
    tasks = Task.objects.filter(status=status)  # Retrieve tasks based on status
    return render(request, 'fetch_task.html', {'tasks': tasks})  # Render partial template


# View to create a new task
def create_task(request):
    """
    Handle the creation of a new task. If the request method is POST, validate and save the new task.
    If the request method is GET, render an empty form.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Populate the form with POST data
        if form.is_valid():
            form.save()  # Save the new task if the form is valid
            return redirect('task_list')  # Redirect to the task list
    else:
        form = TaskForm()  # Render an empty form if the request method is GET
    return render(request, 'create_task.html', {'form': form})  # Render the form template


# View to edit an existing task
def edit_task(request, id):
    """
    Handle editing an existing task. Fetch the task by ID and populate the form with the existing data.
    If the request method is POST, validate and save the updates.
    """
    task = get_object_or_404(Task, pk=id)  # Retrieve the task by ID or return a 404 error
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Populate the form with POST data and existing task data
        if form.is_valid():
            form.save()  # Save the updated task if the form is valid
            return redirect('task_list')  # Redirect to the task list
    else:
        form = TaskForm(instance=task)  # Render the form with existing task data if the request method is GET
    return render(request, 'edit_task.html', {'form': form})  # Render the form template


# View to delete a task
def delete_task(request, id):
    """
    Delete a task by its ID and redirect to the task list.
    """
    task = Task.objects.get(pk=id)  # Retrieve the task by ID
    task.delete()  # Delete the task
    return redirect('task_list')  # Redirect to the task list


# Class-based view for searching tasks
class SearchTask(View):
    """
    Handle searching for tasks based on a query string. Filters tasks by matching the query with
    task descriptions or titles. Returns a template with the search results.
    """
    def get(self, request):
        query = request.GET.get('q', '')  # Get the search query from the request
        tasks = Task.objects.filter(Q(description__icontains=query) | Q(title__icontains=query))  # Filter tasks based on the query
        tasks_data = list(tasks.values('id', 'title', 'description', 'status', 'priority', 'due_date'))  # Convert tasks to a list of dictionaries
        return render(request, 'search_task.html', {'tasks': tasks_data})  # Render the search results template