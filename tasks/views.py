from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task

class TaskListView(APIView):
    """
    get:
    Retorna una lista de todas las tareas.

    post:
    Crea una nueva tarea con los datos proporcionados.
    """
    def get(self, request):
        tasks = Task.objects.all()
        tasks_list = [{'id': task.id, 'name': task.name, 'done': task.done} for task in tasks]
        return Response(tasks_list)

    def post(self, request):
        try:
            data = request.data  # request.data para manejar JSON
            if 'name' not in data or not data['name']:
                return Response({'error': 'Name and done fields are required'}, status=status.HTTP_400_BAD_REQUEST)

            task = Task.objects.create(name=data['name'], done=data.get('done', False))
            return Response({'id': task.id, 'name': task.name, 'done': task.done}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    """
    get:
    Retorna los detalles de una tarea específica.

    put:
    Actualiza una tarea con los datos proporcionados.

    delete:
    Elimina una tarea existente.
    """
    def get(self, request, id):
        try:
            task = Task.objects.get(id=id)
            return Response({'id': task.id, 'name': task.name, 'done': task.done})
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            data = request.data
            task = Task.objects.get(id=id)
            task.name = data.get('name', task.name)
            task.done = data.get('done', task.done)
            task.save()
            return Response({'id': task.id, 'name': task.name, 'done': task.done})
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return Response({'message': 'Task deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
