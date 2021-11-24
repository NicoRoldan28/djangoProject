from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    #Indica el select del combo categoría en las TAREAS
    def __str__(self):
        return '{}'.format(self.name)

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

