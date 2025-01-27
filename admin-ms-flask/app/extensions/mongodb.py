from pymongo import MongoClient
from app.config.config import app_config

class MongoConnection():
    def __init__(self, hostname, port, db, username=None, password=None):
        conn_str = f"mongodb://{hostname}:{port}/{db}"
        self.dbname = db
        self.connection = MongoClient(conn_str)

    def getDb(self):
        return self.connection[self.dbname]

    def close(self):
        pass
        # self.connection.close()


def get_db_connection():
    host = app_config.get("MONGO_HOST")
    port = app_config.get("MONGO_PORT", 27017)
    dbname = app_config.get("MONGO_DBNAME")
    mongo_conn = MongoConnection(host, port, db=dbname)
    return mongo_conn

mongo_con = get_db_connection()