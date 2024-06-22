from flask import Blueprint, request, jsonify
from app.models import Task, User

main_bp = Blueprint('main', __name__)

@main_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    task_id = Task.create_task(data).inserted_id
    return jsonify({"message": "Task created", "task_id": str(task_id)}), 201

@main_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.get_all_tasks()
    return jsonify(tasks), 200

@main_bp.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.get_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

@main_bp.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    Task.update_task(task_id, data)
    return jsonify({"message": "Task updated"}), 200

@main_bp.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    Task.delete_task(task_id)
    return jsonify({"message": "Task deleted"}), 200

@main_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data.get("username") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Username, email, and password are required"}), 400
    user_id = User.create_user(data).inserted_id
    return jsonify({"message": "User created", "user_id": str(user_id)}), 201

@main_bp.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = User.get_user_by_username(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200
