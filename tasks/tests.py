from django.test import TestCase

# Create your tests here.

# Path: tasks/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Task
import json

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(name='Task 1', done=False)
        Task.objects.create(name='Task 2', done=True)

    def test_get_all_tasks(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_add_task(self):
        response = self.client.post(reverse('task_add'), 
            data=json.dumps({'name': 'Task 3', 'done': False}), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Task 3')
        self.assertEqual(response.json()['done'], False)

    def test_delete_task(self):
        response = self.client.delete(reverse('task_delete', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Task deleted')

    def test_update_task(self):
        response = self.client.put(reverse('task_update', args=[2]), 
            data=json.dumps({'name': 'Task 2 Updated', 'done': False}), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Task 2 Updated')
        self.assertEqual(response.json()['done'], False)

