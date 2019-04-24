from api.models import TaskList
from api.serializers import TaskListSerializer2, TasksSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import

class task_list(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    # def get_queryset(self):
    #     return TaskList.objects.all
    
class task_list_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


