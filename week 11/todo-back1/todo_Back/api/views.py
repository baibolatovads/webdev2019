from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .serializers import TaskListSerializer, TaskListSerializer2, TasksSerializer

# Create your views here.
from .models import TaskList, Task


@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        print(serializer.data)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_list, data=data)
        if serializer.is_valid():
            serializer.save()  # update function in serializer class
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({}, status=204)


@csrf_exempt
def task_list_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.task_set.all()
    serializer = TasksSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def task_list_tasks_detail(request, pk, ik):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        tasks = task_list.task_set.all();
        for t in tasks:
            if t.id == ik:
                serializer = TasksSerializer(t)
                return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        tasks = task_list.task_set.all();
        for t in tasks:
            if t.id == ik:
                t.delete()
                return JsonResponse({}, status=204)

    elif request.method == 'PUT':
        tasks = task_list.task_set.all()
        for t in tasks:
            if t.id == ik:
                data = json.loads(request.body)
                serializer = TasksSerializer(instance=t, data=data)
                if serializer.is_valid():
                    serializer.save()  # update function in serializer class
                    return JsonResponse(serializer.data, status=200)
                return JsonResponse(serializer.errors)
