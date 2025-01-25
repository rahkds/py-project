from flask import Blueprint
from ..controllers.admin_controller import get_all

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


admin_bp.add_url_rule('/', view_func=get_all, methods=['GET'])