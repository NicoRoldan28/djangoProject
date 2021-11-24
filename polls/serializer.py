from rest_framework import serializers
from polls.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = fields = ['user', 'name', 'description', 'complete', 'category']