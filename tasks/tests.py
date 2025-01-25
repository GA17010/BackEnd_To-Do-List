from django.test import TestCase
from django.urls import reverse
from .models import Task
import json

# Create your tests here.

class TaskTestCase(TestCase):
    """Pruebas para los endpoints relacionados con tareas"""

    @classmethod
    def setUpTestData(cls):
        """Configura los datos iniciales de prueba (solo se ejecuta una vez por clase)."""
        Task.objects.create(name='Task 1', done=False)
        Task.objects.create(name='Task 2', done=True)

    def test_get_all_tasks(self):
        """Debería retornar todas las tareas en formato JSON."""
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['name'], 'Task 1')
        self.assertEqual(response.json()[1]['done'], True)

    def test_add_task(self):
        """Debería agregar una nueva tarea correctamente."""
        response = self.client.post(
            reverse('task-list'),
            data=json.dumps({'name': 'Task 3', 'done': False}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'Task 3')
        self.assertEqual(response.json()['done'], False)
        # Verificar que la tarea fue almacenada en la base de datos
        self.assertTrue(Task.objects.filter(name='Task 3').exists())

    def test_delete_task(self):
        """Debería eliminar una tarea existente."""
        response = self.client.delete(reverse('task-detail', args=[1]))
        self.assertEqual(response.status_code, 204)
        # Verificar que la tarea fue eliminada de la base de datos
        self.assertFalse(Task.objects.filter(id=1).exists())

    def test_delete_nonexistent_task(self):
        """Debería devolver 404 al intentar eliminar una tarea inexistente."""
        response = self.client.delete(reverse('task-detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_update_task(self):
        """Debería actualizar una tarea existente correctamente."""
        response = self.client.put(
            reverse('task-detail', args=[2]),
            data=json.dumps({'name': 'Task 2 Updated', 'done': False}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Task 2 Updated')
        self.assertEqual(response.json()['done'], False)
        # Verificar que los cambios fueron reflejados en la base de datos
        updated_task = Task.objects.get(id=2)
        self.assertEqual(updated_task.name, 'Task 2 Updated')
        self.assertEqual(updated_task.done, False)

    def test_add_task_invalid_data(self):
        """Debería devolver 400 si los datos enviados son inválidos."""
        response = self.client.post(
            reverse('task-list'),
            data=json.dumps({'done': 'not-a-boolean'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_response_headers(self):
        """Debería verificar que los headers de las respuestas son correctos."""
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
