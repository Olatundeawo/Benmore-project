from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    Form for creating and updating a Task object.
    """
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',  # Use HTML5 date input type for due_date field
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }
        )
    )

    class Meta:
        """
        Meta class specifying the model and fields for the form.
        """
        model = Task  # Specify the Task model for the form
        fields = ['title', 'description', 'category', 'due_date', 'status', 'priority', 'assigned_to']
        # Define the fields to include in the form
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'rows': 4
            }),
            'category': forms.Select(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
            'status': forms.Select(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
            'priority': forms.Select(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
            'assigned_to': forms.Select(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
        }
class TaskFilterForm(forms.Form):
    """
    Form for filtering tasks based on search query, priority, due date, and category.
    """
    q = forms.CharField(required=False, label='Search')  # Search query field
    priority = forms.ChoiceField(
        choices=[('', 'Select Priority'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        required=False  # Priority filter field
    )
    due_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})  # Due date filter field with HTML5 date input type
    )
    category = forms.CharField(required=False, label='Category')  # Category filter field
