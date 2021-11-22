import form as form
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from polls.forms import TaskForm, TaskModelForm, UserRegisterForm
from polls.models import Task
from django.views.generic import ListView, TemplateView

from django.contrib import messages

import user

# class FormListView(ListView)
#   templete_name= 'polls/index.html'
#  queryset = user.object.all()



def all_task(request):
    return render(request,
                  'polls/index.html',
                  {'task': Task.objects.all,
                   'valor': 123123})


class FormTest(FormView):
    template_name = 'form.html'
    success_url = 'index.html'
    form_class = TaskForm

    def form_valid(self, form):
        return super().form_valid(form)





class TaskCreate(CreateView):
    form_class = TaskModelForm
    template_name = 'form.html'
    success_url = 'index.html'


class TaskCreate(CreateView):
    form_class = TaskModelForm
    template_name = 'form.html'
    success_url = reverse_lazy()



class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'description', 'complete']
    template_name = 'polls/form.html'
    success_url = '/polls/task'


class TaskDelete(DeleteView):
    form_class = TaskModelForm
    template_name = 'polls/form.html'
    success_url = '/polls/task'

class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'listTask.html'
    #fields = ['name', 'description', 'complete']
    #template_name = 'listTask.html'
    #success_url = 'listTask.html'


class BienvenidaView(TemplateView):
        template_name = 'Bienvenido.html'

def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            redirect(TaskCreate.as_view())
    elif request.method=='GET':
        form = UserRegisterForm()

    context= {'form': form}
    return render(request, 'perfilForm.html', context)


