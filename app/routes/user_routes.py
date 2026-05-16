from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.user_service import UserService
from app.utils.decorators import admin_required

user_bp = Blueprint("users", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    try:
        user = UserService.register_user(
            email=data["email"],
            username=data["username"],
            password=data["password"]
        )

        return jsonify(
            {
                "msg": f"User {user.email} created", 
                "data": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                    "role": user.role,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at
                },
                "id": user.id}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    try:
        token = UserService.login_user(
            email=data["email"],
            password=data["password"]
        )

        return jsonify({"access_token": token})

    except ValueError as e:
        return jsonify({"error": str(e)}), 401


@user_bp.route("/", methods=["GET"])
@jwt_required()
@admin_required
def get_users():
    users = UserService.get_all_users()

    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role": u.role,
            "created_at": u.created_at,
            "updated_at": u.updated_at
        }
        for u in users
    ])


@user_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    try:
        user = UserService.get_user_by_id(user_id)

        return jsonify(
            {
                "id": user.id, 
                "email": user.email, 
                "username": user.username, 
                "role": user.role,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
        )

    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@user_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    data = request.json

    try:
        user = UserService.update_user(
            user_id,
            email=data.get("email"),
            username=data.get("username"),
            password=data.get("password"),
        )

        return jsonify(
            {
                "id": user.id, 
                "email": user.email, 
                "username": user.username, 
                "role": user.role,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
        )

    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@user_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_user(user_id):
    try:
        UserService.delete_user(user_id)
        return jsonify({"msg": "Deleted"})

    except ValueError as e:
        return jsonify({"error": str(e)}), 404