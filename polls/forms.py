import self as self
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from polls.models import Task, Category


class TaskModelForm(ModelForm):


    class Meta:
        model = Task
        fields = ['user', 'name', 'description', 'complete', 'category']

    # Ejemplo de inicializar un valor, no funciono para user
    #def __init__(self, *args, **kwargs):
    #   super(TaskModelForm, self).__init__(*args, **kwargs)
        #    self.fields['user'].widget.attrs = {
        #   'initial': 1,
        #   'readonly': False,
        #   'placeholder': 'Ejemplo de placeholder',
        #   'required': True
        #}


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

class CategoryModelForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


