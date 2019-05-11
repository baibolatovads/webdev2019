from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskListManager(models.Manager):
    def for_user(self, user):
        self.filter(created_by = user).order_by('name')


class TaskList(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    objects = TaskListManager()

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    task_list = models.ForeignKey(TaskList, on_delete = models.CASCADE, related_name='tasks')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created at': self.created_at,
            'due on': self.due_on
        }