from pymongo import MongoClient
from app.extensions.mongodb import MongoConnection
from app.utils.file import FileUitl 
import os



def run_db_changes(db: MongoClient):
    pass



def migrate_up(conn : MongoConnection):
    script_file = os.path.join(os.path.dirname(__file__), "../schema-data/20250203120220-create-initial-schema.js")
    FileUitl.execute_mongo_script(script_file, conn)
    return

    # db = conn.getDb()
    # collections = db.list_collection_names()
    # if not "admin_users" in collections:
    #     validator = {
    #         "$jsonSchema": {
    #             "bsonType": "object",
    #             "required": ["email", "username"],
    #             "properties": {
    #                 "email": {
    #                     "bsonType": "string",
    #                     "description": "must be a string and is required"
    #                 },
    #                 "username": {
    #                     "bsonType": "string",
    #                     "description": "must be a string and is required"
    #                 }
    #             }
    #         }
    #     }

    #     db.command("create", "admin_users", validator=validator, validationLevel="strict", validationAction="error")
    #     db.admin_users.create_index([("email", 1)], unique=True)

    #  if not "acl_roles" in collections:
    #     validator = {
    #             "$jsonSchema" : {
    #                 "bsonType" : "object", 
    #                 "required" : ["role_name"],
    #                 "properties" : {
    #                     "role_name" : {
    #                         "bsonType" : "string",
    #                         "description" : "must be a string and is required"
    #                     }
    #                 }
    #         }
    #     }
    #     db.command("create", "acl_roles", validator=validator, validationLevel="strict", validationAction="error")
    #     db.acl_roles.create_index([("role_name", 1)], unique=True)


def migrate_down():
    pass