from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from api.models import Task1, TaskList1
from django.shortcuts import get_object_or_404

def task_lists(request):
    task_list = TaskList1.objects.all()
    json_tasks = [t.to_json() for t in task_list]
    return JsonResponse(json_tasks, safe=False)


def task_detail(request, pk):
    #try:
     #   task_list = TaskList1.objects.get(id=pk)
    #except TaskList1.DoesNotExist as e:
     #   return JsonResponse({'error': str(e)})

    task_list = get_object_or_404(TaskList1, id = pk)
    return JsonResponse(task_list.to_json())


def tasks(request, pk):
    #try:
     #   task_list = TaskList1.objects.get(id=pk)
    #except TaskList1.DoesNotExist as e:
     #   return JsonResponse({'error': str(e)})

#    tasks = Task1.tasks_set.all()
 #   json_task = [t.to_json() for t in tasks]

    task_list = get_object_or_404(TaskList1, id = pk)
    tasks = task_list.task_set.all()
    json_task = [t.to_json() for t in tasks]
    return JsonResponse(json_task, safe=False)

def index(request):
    return HttpResponse("Hello World")