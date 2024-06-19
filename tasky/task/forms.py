from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
            widget=forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority', 'assigned_to']



class TaskFilterForm(forms.Form):
    q = forms.CharField(required=False, label='Search')
    priority = forms.ChoiceField(choices=[('', 'Select Priority'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], required=False)
    due_date =  forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.CharField(required=False, label='Category')