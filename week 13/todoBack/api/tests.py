from django.test import TestCase
from django.test import Client
from rest_framework.response import Response
from .models import TaskList
# Create your tests here.

def test_board_list_200(db, client: Client, task_list: TaskList) -> None:
    response: Response = client.get(path='task_lists/')
    assert len(response.data) == 4
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['id'] == task_list.id
    assert response.data['results'][0]['name'] == 'taskList'
    return 'ok'


