from pymongo import MongoClient
from app.config.config import app_config

class MongoConnection():
    def __init__(self, hostname, port, db, username=None, password=None):
        conn_str = f"mongodb://{hostname}:{port}/{db}"
        self.connection = MongoClient(conn_str)


def get_mongo_connection():
    host = app_config.get("MONGO_HOST")
    port = app_config.get("MONGO_PORT", 27017)
    dbname = app_config.get("MONGO_DBNAME")
    return MongoConnection(host, port, db=dbname)