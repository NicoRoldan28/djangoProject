from django import forms
from django.forms import ModelForm

from polls.models import Task

class TaskModelForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'complete']


class TaskForm(forms.Form):
    name= forms.CharField(widget=forms.CharField)
    description = forms.CharField(widget=forms.Textarea)
    complete= forms.BooleanField()

    def post(self):
        print("hello")
