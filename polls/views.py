from django.shortcuts import render

# Create your views here.
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.views.generic import ListView

import user

# class FormListView(ListView)
#   templete_name= 'polls/index.html'
#  queryset = user.object.all()
from polls.forms import TaskForm, TaskModelForm
from polls.models import Task


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


