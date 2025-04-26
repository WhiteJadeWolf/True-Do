from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter task name'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'rows': 4, 'placeholder': 'Describe your task'}),
        }
