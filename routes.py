from flask import Flask
from flask_jwt_extended import JWTManager
from src.controllers.user_controller import user_bp
from src.controllers.login_controller import login_bp


def create_app():
    app = Flask(__name__)

    # Recomendado armazenar essas informações em um arquivo .env
    app.config["JWT_SECRET_KEY"] = "1234"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    jwt = JWTManager(app)

    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(login_bp, url_prefix="/auth")

    return app
