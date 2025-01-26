from flask import Blueprint
from ..controllers.admin_controller import get_all, create
from app.validators.admin_validator import CreateAdminSchema
from app.middlewares.validate import validate_request_schema

admin_bp = Blueprint('admins', __name__, url_prefix='/admins')

admin_bp.add_url_rule('/', view_func=get_all, methods=['GET'])

admin_bp.add_url_rule('/', view_func=validate_request_schema(CreateAdminSchema)(create), methods=['POST'])