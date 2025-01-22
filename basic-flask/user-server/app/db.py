import mysql.connector # type: ignore
import os

class MysqlConnection:
    def __init__(self,user, password, port, host, db):
        self.connection = mysql.connector.connect(user=user, password=password, 
                                                  host=host, port=port, database=db)
        
    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(buffered=True,dictionary=True)
        cursor.execute(query, params)
        return cursor
    
    def close(self):
        self.connection.close()
    

def get_mysql_connection():
    host = os.environ.get('MYSQL_DB_HOST')
    username = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASS')
    port = os.environ.get('PORT', 3306)
    return MysqlConnection(username, password, port, host, 'py_flask')
        
    