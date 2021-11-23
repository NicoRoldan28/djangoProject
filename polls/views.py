from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from polls.forms import TaskForm, TaskModelForm, UserRegisterForm, CategoryModelForm
from polls.models import Task, Category
from django.views.generic import ListView, TemplateView

from django.contrib import messages

import user


# class FormListView(ListView)
#   templete_name= 'polls/index.html'
#  queryset = user.object.all()


def all_task(request):
    return render(request,
                  'polls/index.html',
                  {'task': Task.objects.all()}
                  )


class FormTest(FormView):
    template_name = 'formTask.html'
    success_url = 'index.html'
    form_class = TaskForm

    def form_valid(self, form):
        return super().form_valid(form)


# ----------- TASK -----------#

class TaskCreate(CreateView):
    form_class = TaskModelForm
    template_name = 'formTask.html'
    success_url = reverse_lazy('create_task')

    # Create y Update, no necesitan success_url


class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'description', 'complete']
    template_name = 'polls/formTask.html'
    success_url = '/polls/task'


class TaskDelete(DeleteView):
    form_class = TaskModelForm
    template_name = 'polls/formTask.html'
    success_url = '/polls/task'


class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'listTask.html'
    # fields = ['name', 'description', 'complete']
    # template_name = 'listTask.html'
    # success_url = 'listTask.html'


# ----------- CATEGORY -----------#

class CategoryCreate(CreateView):
    form_class = CategoryModelForm
    template_name = 'formCategory.html'
    # success_url = reverse_lazy('CreateView')


class CategoryList(ListView):
    model = Task
    context_object_name = 'category'
    template_name = 'listCategory.html'
    queryset = Category.objects.all()


# ----------- WELCOME -----------#

class WelcomeView(TemplateView):
    template_name = 'Welcome.html'


# ----------- LOGIN -----------#

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            redirect(WelcomeView.as_view())
    elif request.method == 'GET':
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'perfilForm.html', context)
