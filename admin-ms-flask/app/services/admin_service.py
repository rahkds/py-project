from app.extensions.mongodb import mongo_con
from bson  import ObjectId
from app.utils.common import CustomJSONEncoder
import json

def get_list():
    return list(mongo_con.getDb().admin_users.find())

def create_admin(admin_data):
    mongo_con.getDb().admin_users.insert_one(admin_data)

def check_admin_by_email(email):
    count = mongo_con.getDb().admin_users.count_documents({"email" : email})
    return True if count else False

def get_admin_by_id(admin_id):
    return mongo_con.getDb().admin_users.find_one({"_id" : ObjectId(admin_id)})

def update_admin(admin_data, admin_id):
    mongo_con.getDb().admin_users.update_one({"_id" : ObjectId(admin_id)}, {"$set" : admin_data})

def delete_admin(admin_id):
    mongo_con.getDb().admin_users.delete_one({"_id" : ObjectId(admin_id)})

def assign_role(admin_id, role_data):
    for role in role_data.get("roles", []):
        role['role_id'] = ObjectId(role['role_id'])

    mongo_con.getDb().admin_users.update_one({"_id" : ObjectId(admin_id)}, {"$set" : role_data})
