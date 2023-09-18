from flask import Blueprint, request, jsonify
from src.models.user_model import UserModel
from src.views.user_view import view_create_user, view_get_all_users, view_delete_user

user_bp = Blueprint("user", __name__)


@user_bp.route("/create-user", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados JSON ausentes no corpo da solicitação"}), 400

        user_id = data.get("user_id")
        email = data.get("email")
        senha = data.get("senha")

        if not user_id or not email or not senha:
            return jsonify({"error": "Campos obrigatórios ausentes"}), 400

        if UserModel.create_user(user_id, email, senha):
            return view_create_user()
        else:
            return jsonify({"error": "Erro ao criar usuário"}), 500
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@user_bp.route("/get-users", methods=["GET"])
def get_users():
    try:
        users = UserModel.get_all_users()
        return view_get_all_users(users)
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@user_bp.route("/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        UserModel.delete_user(user_id)
        return view_delete_user()
    except Exception as error:
        return jsonify({"error": str(error)}), 500
