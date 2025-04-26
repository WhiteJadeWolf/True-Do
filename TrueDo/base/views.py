from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task
from .forms import TaskForm

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
class SignupPage(FormView):
    template_name = 'base/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupPage, self).form_valid(form)
    
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'mytasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mytasks'] = context['mytasks'].filter(user=self.request.user)
        context['count'] = context['mytasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['mytasks'] = context['mytasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        return context
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'base/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'base/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'base/task_confirm_delete.html'
    fields = '__all__'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')