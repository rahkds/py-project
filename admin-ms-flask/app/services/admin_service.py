from app.extensions.mongodb import get_mongo_connection
from bson  import json_util
from app.utils.common import CustomJSONEncoder
import json

def get_list():
    conn = get_mongo_connection()
    cursor = conn.connection.cash_platform_admin.admin_users.find()
   # json_string = json_util.dumps(list(admin_list), cls=CustomJSONEncoder)
    json_string = json.dumps(list(cursor),cls=CustomJSONEncoder)
    admin_list = json.loads(json_string)
    cursor.close()
    conn.close
    return admin_list
    