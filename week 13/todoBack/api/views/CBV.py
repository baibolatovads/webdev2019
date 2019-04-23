from api.models import TaskList
from api.serializers import TaskListSerializer2, TasksSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class task_list(APIView):
    def get(self, request):
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class task_list_detail(APIView):

    def get_object(self, pk):
        try:
            return True, TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            return False, Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        found, task_list = self.get_object(pk)
        if found:
            serializer = TaskListSerializer2(task_list)
            return Response(serializer.data)
        return task_list

    def put(self, request, pk):
        found, task_list = self.get_object(pk)
        serializer = TaskListSerializer2(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        found, task_list = self.get_object(pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class task_list_tasks(APIView):

    def get_object(self, pk):
        try:
            return True, TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist as e:
            return False, Response({'error': str(e)})

    def get(self, request, pk):
        found, task_list = self.get_object(pk)
        if found:
            tasks = task_list.task_set.all()
            serializer = TasksSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return task_list


class task_list_tasks_detail(APIView):

    def get_object(self, pk):
        try:
            return True, TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist as e:
            return False, Response({'error': str(e)})

    def get(self, request, pk, pk1):
        found, task_list = self.get_object(pk)
        if found:
            tasks = task_list.task_set.all()
            for t in tasks:
                if t.id == pk1:
                    serializer = TasksSerializer(t)
                    return Response(serializer.data)
        return task_list

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors)

    def delete(self, request, pk1):
        found, task_list = self.get_object(pk1)
        if found:
            tasks = task_list.task_set.all()
            for t in tasks:
                if t.id == pk1:
                    t.delete()
                    return Response({}, status=204)
        return task_list

    def put(self, request, pk, pk1):
        found, task_list = self.get_object(pk)
        if found:
            tasks = task_list.task_set.all()
            for t in tasks:
                if t.id == pk1:
                    serializer = TasksSerializer(instance=t, data=request.data)
                    if serializer.is_valid():
                        serializer.save()  # update function in serializer class
                        return Response(serializer.data, status=200)
                    return Response(serializer.errors)
        return task_list

