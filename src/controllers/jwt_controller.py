from flask import jsonify
from flask_jwt_extended import create_access_token, verify_jwt_in_request, JWTManager


jwt = JWTManager()


def generate_token(email):
    access_token = create_access_token(identity=email)
    return access_token


def token_required(func):

    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return func(*args, **kwargs)
        except Exception as error:
            return jsonify({"error": "Token inválido ou expirado"}), 401

    return wrapper
