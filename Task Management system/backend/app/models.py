from flask_pymongo import ObjectId
from app import mongo

class Task:
    @staticmethod
    def create_task(data):
        task = {
            "title": data["title"],
            "description": data.get("description", ""),
            "assigned_to": data.get("assigned_to"),
            "deadline": data.get("deadline"),
            "status": "Pending"
        }
        return mongo.db.tasks.insert_one(task)

    @staticmethod
    def get_all_tasks():
        return list(mongo.db.tasks.find())

    @staticmethod
    def get_task(task_id):
        return mongo.db.tasks.find_one({"_id": ObjectId(task_id)})

    @staticmethod
    def update_task(task_id, data):
        return mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data})

    @staticmethod
    def delete_task(task_id):
        return mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})

class User:
    @staticmethod
    def create_user(data):
        user = {
            "username": data["username"],
            "email": data["email"],
            "password": data["password"]  # For simplicity, not hashed in this example
        }
        return mongo.db.users.insert_one(user)

    @staticmethod
    def get_user_by_username(username):
        return mongo.db.users.find_one({"username": username})
