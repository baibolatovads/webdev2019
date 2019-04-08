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
    created_at = models.DateTimeField
    due_on = models.DateTimeField
    status = models.CharField
    task_list = models.ForeignKey

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }