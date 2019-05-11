from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TasksSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.filters import TaskFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class task_list1(generics.ListCreateAPIView):
    #queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    # def get_queryset(self):
    #     return TaskList.objects.all
    permission_classes = (IsAuthenticated, )
    filter_backends = (SearchFilter,)
    search_fields=('name',)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2    

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


class task_list_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2

class tasks(generics.ListCreateAPIView):
    serializer_class = TasksSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    #filterset_fields = ('name')
    filter_class = TaskFilter
    search_fields = ('name')
    ordering_fields = ('name')
    ordering = ('name')

    def get_queryset(self):
        task_list = get_object_or_404(TaskList, id = self.kwargs.get('pk'))
        # try:
        #     task_list = TaskList.objects.get(id=self.kwargs['pk'])
        # except TaskList.DoesNotExist:
        #     raise Http404
        queryset = task_list.tasks.all()
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     queryset = queryset.filter(name = name)
        return queryset

