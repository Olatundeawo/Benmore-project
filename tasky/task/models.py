from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    """
    Model representing a task.
    """
    # Choices for the status of the task
    STATUS_CHOICES = [
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    # Choices for the priority of the task
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    CATEGORY_CHOICES = [
        ('UX Design', 'UX Design'),
        ('Development', 'Developement'),
    ]

    # Fields of the Task model
    title = models.CharField(max_length=255)  # Title of the task
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES, default='developement')  # Category of the task
    description = models.TextField(blank=True, null=True)  # Description of the task
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the task was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the task was last updated
    due_date = models.DateTimeField(blank=True, null=True)  # Due date of the task
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='not started')  # Status of the task
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')  # Priority of the task
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='task')  # User to whom the task is assigned

    def __str__(self):
        """
        String representation of the Task object.
        """
        return self.title

    class Meta:
        """
        Metadata options for the Task model.
        """
        ordering = ['due_date', 'created_at']  # Default ordering of tasks
