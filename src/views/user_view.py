from flask import jsonify


def create_user():
    return jsonify({'message': 'Usuário criado com sucesso!'}), 201


def get_all_users(users):
    return jsonify({'message': 'Lista de todos os usuários', 'data': users})


def login_user():
    return jsonify({'message': 'Login bem-sucedido!'})


def delete_user():
    return jsonify({'message': 'Usuário deletado com sucesso!'})
