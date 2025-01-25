from flask import Flask
from app.config.config import app_config
from app.routes.admin_route import admin_bp

def create_app():
    app = Flask('admin-ms')
    app.register_blueprint(admin_bp)
    return app
