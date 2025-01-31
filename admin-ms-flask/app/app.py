from flask import Flask
from app.routes.admin_route import admin_bp
from app.routes.role_route import role_bp
from app.middlewares import register_middleware

def create_app():
    app= Flask('admin-ms')
    register_middleware(app)
    app.register_blueprint(admin_bp)
    app.register_blueprint(role_bp)
    return app
