import unittest
from app import create_app, mongo
from app.services import TaskService, UserService

class ServicesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_URI'] = 'mongodb://localhost:27017/taskmaster_test'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            mongo.db.tasks.delete_many({})
            mongo.db.users.delete_many({})

    def test_task_service_create(self):
        task_data = {
            "title": "Service Test Task",
            "description": "Task description",
            "assigned_to": "serviceuser",
            "deadline": "2023-12-31"
        }
        task_id = TaskService.create_task(task_data)
        self.assertIsNotNone(task_id)

    def test_task_service_get(self):
        task_data = {
            "title": "Service Test Task",
            "description": "Task description",
            "assigned_to": "serviceuser",
            "deadline": "2023-12-31"
        }
        task_id = TaskService.create_task(task_data)
        task = TaskService.get_task(task_id)
        self.assertIsNotNone(task)
        self.assertEqual(task['title'], task_data['title'])

    def test_user_service_create(self):
        user_data = {
            "username": "serviceuser",
            "email": "service@example.com",
            "password": "password123"
        }
        user_id = UserService.create_user(user_data)
        self.assertIsNotNone(user_id)

    def test_user_service_get(self):
        user_data = {
            "username": "serviceuser",
            "email": "service@example.com",
            "password": "password123"
        }
        UserService.create_user(user_data)
        user = UserService.get_user_by_username(user_data['username'])
        self.assertIsNotNone(user)
        self.assertEqual(user['email'], user_data['email'])

if __name__ == '__main__':
    unittest.main()
