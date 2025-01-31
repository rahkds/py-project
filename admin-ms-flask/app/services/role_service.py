from app.extensions.mongodb import mongo_con
from bson import ObjectId

def get_list():
    return list(mongo_con.getDb().acl_roles.find())

def create_role(role_data):
    mongo_con.getDb().acl_roles.insert_one(role_data)

def check_role_by_name(role_name):
    count = mongo_con.getDb().acl_roles.count_documents({"role_name" : role_name})
    return True if count else False

def get_role_by_id(role_id):
    return mongo_con.getDb().acl_roles.find_one({"_id" : ObjectId(role_id)})

def update_role(role_data, role_id):
    mongo_con.getDb().acl_roles.update_one({"_id" : ObjectId(role_id)}, {"$set" : role_data})

def delete_role(role_id):
    mongo_con.getDb().acl_roles.delete_one({"_id" : ObjectId(role_id)})
