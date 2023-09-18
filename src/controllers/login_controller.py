from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from src.models.user_model import UserModel
from src.views.user_view import view_login_user

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados JSON ausentes no corpo da solicitação"}), 400

        email = data.get("email")
        senha = data.get("senha")

        if not email or not senha:
            return jsonify({"error": "Campos obrigatórios ausentes"}), 400

        users = UserModel.login_user(email, senha)
        if users:
            access_token = create_access_token(identity=email)
            return view_login_user(access_token)
        else:
            return jsonify({"error": "Login falhou. Verifique suas credenciais"}), 401
    except Exception as error:
        return jsonify({"error": str(error)}), 500
