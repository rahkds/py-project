from flask import Blueprint
from ..controllers.admin_controller import get_admins, create_admin, get_admin, update_admin, delete_admin
from app.validators.admin_validator import CreateAdminSchema, UpdateAdminSchema
from app.middlewares.validate import validate_request_schema

admin_bp = Blueprint('admins', __name__, url_prefix='/admins')


@admin_bp.route('/',  methods=['GET'])
def get_all():
    return get_admins()


@admin_bp.route('/',  methods=['POST'], endpoint='create_admin')
@validate_request_schema(CreateAdminSchema)
def create():
    return create_admin()


@admin_bp.route('/<admin_id>',  methods=['GET'])
def get(admin_id):
    return get_admin(admin_id)


@admin_bp.route('/<admin_id>',  methods=['PUT'], endpoint='update_admin')
@validate_request_schema(UpdateAdminSchema)
def update(admin_id):
    return update_admin(admin_id)

@admin_bp.route('/<admin_id>',  methods=['DELETE'], endpoint='delete_admin')
def delete(admin_id):
    return delete_admin(admin_id)


