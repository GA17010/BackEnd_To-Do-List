from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task

# Get all tasks
@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_list = list(tasks.values('id', 'name', 'done'))
        return JsonResponse(tasks_list, safe=False)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# Add a task
@csrf_exempt
def task_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            task = Task.objects.create(name=data['name'], done=data['done'])
            return JsonResponse({'id': task.id, 'name': task.name, 'done': task.done})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# Delete a task
@csrf_exempt
def task_delete(request, id):
    if request.method == 'DELETE':
        try:
            print("This is my id task", id)
            task = Task.objects.get(id=id)
            task.delete()
            return JsonResponse({'message': 'Task deleted'})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

# Update a task
@csrf_exempt
def task_update(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            task = Task.objects.get(id=id)
            task.name = data['name']
            task.done = data['done']
            task.save()
            return JsonResponse({'id': task.id, 'name': task.name, 'done': task.done})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
