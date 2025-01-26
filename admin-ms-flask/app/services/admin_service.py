from app.extensions.mongodb import get_db_connection
from bson  import json_util
from app.utils.common import CustomJSONEncoder
import json

def get_list():
    conn = get_db_connection()
    cursor = conn.getDb().admin_users.find()
   # json_string = json_util.dumps(list(admin_list), cls=CustomJSONEncoder)
    json_string = json.dumps(list(cursor),cls=CustomJSONEncoder)
    admin_list = json.loads(json_string)
    cursor.close()
    conn.close()
    return admin_list

def create_admin(admin_data):
    conn = get_db_connection()
    conn.getDb().admin_users.insert_one(admin_data)
    conn.close()   


def check_admin_by_email(email):
    conn = get_db_connection()
    count = conn.getDb().admin_users.count_documents({"email" : email})
    return True if count else False