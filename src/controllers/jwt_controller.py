from functools import wraps
from flask import jsonify, request
from flask_jwt_extended import create_access_token, verify_jwt_in_request, JWTManager, get_jwt_identity


jwt = JWTManager()


def generate_token(email):
    access_token = create_access_token(identity=email)
    return access_token


def token_required(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        raw_token = request.headers.get('Authorization')
        email = request.headers.get('email')

        if not raw_token or not email:
            return jsonify({
                'error': 'Não autorizado'
            }), 401

        try:
            token = raw_token.split()[1]
            verify_jwt_in_request(optional=True)
            current_email = get_jwt_identity()
        except Exception as error:
            return jsonify({
                'error': 'Token inválido'
            }), 401

        if email != current_email:
            return jsonify({
                'error': 'Usuário não permitido'
            }), 401

        return function(*args, **kwargs)

    return decorated
