from flask import request, Blueprint,jsonify
from .db import get_mysql_connection

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    conn = get_mysql_connection()
    cursor = conn.execute_query("SELECT * FROM users")
    all_users = cursor.fetchall()
    cursor.close()
    conn.close()
    return {
        "status": True,
        "data" : all_users
    }

@user_bp.route('/', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_name = user_data.get('name')
    user_email = user_data.get('email')

    if not user_name or not user_email:
        return {"status" : False, "msg" : "name and email is mandatory fields"}, 400

    conn = get_mysql_connection()
    cursor = conn.execute_query("INSERT INTO users (name, email) VALUES (%s, %s)", (user_name, user_email))
    conn.connection.commit()
    cursor.close()
    conn.close()
    return { "status": True, "msg" : "User successfully created"}



@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_mysql_connection()
    cursor = conn.execute_query("SELECT * FROM users WHERE id = %s", (id,))
    user_info = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user_info:
        return {"status": False,"msg" : "user not found"}
    else :
        return {"status": True,"data" : user_info}
    


@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_mysql_connection()
    cursor = conn.execute_query("DELETE FROM users WHERE id = %s", (id,))
    conn.connection.commit()
    cursor.close()
    conn.close()
    return {"status": True,"msg" : "user deleted"}
    



