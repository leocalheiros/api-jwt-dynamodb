from flask import jsonify


def view_create_user():
    return jsonify({'message': 'Usuário criado com sucesso!'}), 201


def view_get_all_users(users):
    return jsonify({'message': 'Lista de todos os usuários', 'data': users})


def view_login_user():
    return jsonify({'message': 'Login bem-sucedido!'})


def view_delete_user():
    return jsonify({'message': 'Usuário deletado com sucesso!'})
