from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)

# Create your models here.
