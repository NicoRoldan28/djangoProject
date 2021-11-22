from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from polls.models import Task

class TaskModelForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'complete']


class TaskForm(forms.Form):
    name = forms.CharField(widget=forms.CharField)
    description = forms.CharField(widget=forms.Textarea)
    complete= forms.BooleanField()

    def post(self):
        print("hello")

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
        help_texts = {k:"" for k in fields}





