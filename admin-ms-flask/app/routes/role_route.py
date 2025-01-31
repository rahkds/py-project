from flask import Blueprint
from ..controllers.role_controller import get_roles, create_role, get_role, update_role, delete_role
from app.validators.role_validator import CreateRoleSchema, UpdateRoleSchema
from app.middlewares.validate import validate_request_schema

role_bp = Blueprint('roles', __name__, url_prefix='/roles')


@role_bp.route('/',  methods=['GET'])
def get_all():
    return get_roles()


@role_bp.route('/',  methods=['POST'], endpoint='create_role')
@validate_request_schema(CreateRoleSchema)
def create():
    return create_role()


@role_bp.route('/<role_id>',  methods=['GET'])
def get(role_id):
    return get_role(role_id)


@role_bp.route('/<role_id>',  methods=['PUT'], endpoint='update_role')
@validate_request_schema(UpdateRoleSchema)
def update(role_id):
    return update_role(role_id)

@role_bp.route('/<role_id>',  methods=['DELETE'], endpoint='delete_role')
def delete(role_id):
    return delete_role(role_id)


