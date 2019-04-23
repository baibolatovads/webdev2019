from django.db import models

# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=255)
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
    task_list = models.ForeignKey(TaskList, on_delete = models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created at': self.created_at,
            'due on': self.due_on
        }