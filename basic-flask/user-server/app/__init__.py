from flask import Flask
from .routes import user_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app

