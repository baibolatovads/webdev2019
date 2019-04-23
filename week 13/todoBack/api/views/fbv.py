from api.models import TaskList
from api.serializers import TaskListSerializer2, TasksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id = pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer2(task_list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer2(instance = task_list, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def task_list_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error': str(e)})

    tasks = task_list.task_set.all()
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def task_list_tasks_detail(request, pk, ik):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        tasks = task_list.task_set.all();
        for t in tasks:
            if t.id == pk:
                serializer = TasksSerializer(t)
                return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        tasks = task_list.task_set.all();
        for t in tasks:
            if t.id == pk:
                t.delete()
                return Response({}, status=204)

    elif request.method == 'PUT':
        tasks = task_list.task_set.all()
        for t in tasks:
            if t.id == pk:
                serializer = TasksSerializer(instance=t, data=request.data)
                if serializer.is_valid():
                    serializer.save()  # update function in serializer class
                    return Response(serializer.data, status=200)
                return Response(serializer.errors)
