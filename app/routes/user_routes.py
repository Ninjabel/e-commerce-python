from flask import Blueprint, jsonify, request
from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.get_all_users()
    return jsonify([{"user_id": user.user_id, "username": user.username, "email": user.email} for user in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return jsonify({"user_id": user.user_id, "username": user.username, "email": user.email})
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(User.users_db) + 1
    username = data.get('username')
    email = data.get('email')
    if username and email:
        new_user = User(user_id, username, email)
        return jsonify({"message": "User created", "user_id": new_user.user_id}), 201
    return jsonify({"message": "Invalid data"}), 400

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if User.delete_user(user_id):
        return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if User.update_user(user_id, username, email):
        return jsonify({"message": "User updated"})
    return jsonify({"message": "User not found"}), 404