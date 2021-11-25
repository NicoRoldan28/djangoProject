from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.db import models
from enum import Enum

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

    class StatusDomain(models.TextChoices):
        PRC = 'PRC', _('In Progress')
        TDO = 'TDO', _('To Do')
        OK = 'OK', _('Done')
        NDO = 'NDO', _('Not To Do')

    status = models.CharField(
        max_length=3,
        choices=StatusDomain.choices,
        default=StatusDomain.PRC,
    )

    def is_upperclass(self):
        return self.status in {
            self.status.PRC
        }


