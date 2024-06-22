import unittest
from app import create_app, mongo
from app.models import Task, User

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_URI'] = 'mongodb://localhost:27017/taskmaster_test'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            mongo.db.tasks.delete_many({})
            mongo.db.users.delete_many({})

    def test_create_task(self):
        task_data = {
            "title": "Test Task",
            "description": "Task description",
            "assigned_to": "user1",
            "deadline": "2023-12-31"
        }
        task_id = Task.create_task(task_data).inserted_id
        self.assertIsNotNone(task_id)

    def test_get_task(self):
        task_data = {
            "title": "Test Task",
            "description": "Task description",
            "assigned_to": "user1",
            "deadline": "2023-12-31"
        }
        task_id = Task.create_task(task_data).inserted_id
        task = Task.get_task(str(task_id))
        self.assertIsNotNone(task)
        self.assertEqual(task['title'], task_data['title'])

    def test_update_task(self):
        task_data = {
            "title": "Test Task",
            "description": "Task description",
            "assigned_to": "user1",
            "deadline": "2023-12-31"
        }
        task_id = Task.create_task(task_data).inserted_id
        updated_data = {"title": "Updated Task"}
        Task.update_task(str(task_id), updated_data)
        updated_task = Task.get_task(str(task_id))
        self.assertEqual(updated_task['title'], updated_data['title'])

    def test_delete_task(self):
        task_data = {
            "title": "Test Task",
            "description": "Task description",
            "assigned_to": "user1",
            "deadline": "2023-12-31"
        }
        task_id = Task.create_task(task_data).inserted_id
        Task.delete_task(str(task_id))
        task = Task.get_task(str(task_id))
        self.assertIsNone(task)

    def test_create_user(self):
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
        user_id = User.create_user(user_data).inserted_id
        self.assertIsNotNone(user_id)

    def test_get_user_by_username(self):
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
        User.create_user(user_data)
        user = User.get_user_by_username(user_data['username'])
        self.assertIsNotNone(user)
        self.assertEqual(user['email'], user_data['email'])

if __name__ == '__main__':
    unittest.main()
