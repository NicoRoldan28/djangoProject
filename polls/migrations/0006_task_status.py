# Generated by Django 3.2.9 on 2021-11-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('PRC', 'In Progress'), ('OK', 'Done'), ('TDO', 'To Do'), ('NDO', 'Not To Do')], default='PRC', max_length=3),
        ),
    ]