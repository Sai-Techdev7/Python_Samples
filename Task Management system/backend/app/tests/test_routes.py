import unittest
from app import create_app, mongo
from flask import json

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_URI'] = 'mongodb://localhost:27017/taskmaster_test'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            mongo.db.tasks.delete_many({})
            mongo.db.users.delete_many({})

    def test_create_task(self):
        response = self.client.post('/tasks', json={
            "title": "Test Task",
            "description": "Task description",
            "assigned_to": "user1",
            "deadline": "2023-12-31"
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('task_id', data)

    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post('/users', json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('user_id', data)

if __name__ == '__main__':
    unittest.main()
