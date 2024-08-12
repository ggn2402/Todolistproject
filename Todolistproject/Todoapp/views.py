
# Create your views here.

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task

# Task list view
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

# Task detail view
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'Todoapp/task.html'

# Task create view
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'  # Consider specifying fields explicitly for security
    success_url = reverse_lazy('tasks')  # Ensure 'tasks' is a valid URL name

# Task update view
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'  # Consider specifying fields explicitly for security
    success_url = reverse_lazy('tasks')  # Ensure 'tasks' is a valid URL name

