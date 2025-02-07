from flask import Flask
from app.routes.admin_route import admin_bp
from app.routes.role_route import role_bp
from app.middlewares import register_middleware
from app.migrations.migration import applyMigrations


def bootstrap(app : Flask):
    register_middleware(app)
    app.register_blueprint(admin_bp)
    app.register_blueprint(role_bp)
    applyMigrations()


def create_app():
    app= Flask('admin-ms')
    bootstrap(app)
    return app
