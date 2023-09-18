from flask import Flask
from src.controllers.user_controller import user_bp
from src.controllers.login_controller import login_bp


def create_app():
    app = Flask(__name__)

    # Registrar os Blueprints
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(login_bp, url_prefix="/auth")

    return app
