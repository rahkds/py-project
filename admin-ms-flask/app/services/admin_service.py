from app.extensions.mongodb import get_mongo_connection
from bson  import json_util

def get_list():
    conn = get_mongo_connection()
    admin_list = conn.connection.cash_platform_admin.admin_users.find()
    return json_util.dumps(admin_list)
    