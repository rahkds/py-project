from app.services import admin_service
from app.utils.api_response import APIResponse
from flask import request

def get_admins():
    admin_data =  admin_service.get_list()
    return APIResponse.success(admin_data)

def create_admin():
    admin_data = request.get_json()
    admin_exists = admin_service.check_admin_by_email(admin_data['email'])
    if admin_exists:
        return APIResponse.validation_error(message='admin already exists')
    admin_service.create_admin(admin_data)
    return APIResponse.success()

def get_admin(admin_id):
    admin_data = admin_service.get_admin_by_id(admin_id)
    if not admin_data:
        return APIResponse.validation_error(message="Admin doesn't exists")
    return APIResponse.success(admin_data)

def update_admin(admin_id):
    admin_data = request.get_json()
    admin_service.update_admin(admin_data, admin_id)
    return APIResponse.success()

def delete_admin(admin_id):
    admin_service.delete_admin(admin_id)
    return APIResponse.success()

def assign_role(admin_id):
    admin_data = admin_service.get_admin_by_id(admin_id)
    if not admin_data:
        return APIResponse.validation_error(message="Admin doesn't exists")    
    role_data = request.get_json()
    admin_service.assign_role(admin_id, role_data)
    return APIResponse.success()

