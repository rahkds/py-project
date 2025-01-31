from app.services import role_service
from app.utils.api_response import APIResponse
from flask import request

def get_roles():
    role_data =  role_service.get_list()
    return APIResponse.success(role_data)

def create_role():
    role_data = request.get_json()
    role_exists = role_service.check_role_by_name(role_data['role_name'])
    if role_exists:
        return APIResponse.validation_error(message='Role already exists')
    role_service.create_role(role_data)
    return APIResponse.success()

def get_role(role_id):
    role_data = role_service.get_role_by_id(role_id)
    if not role_data:
        return APIResponse.validation_error(message="Role doesn't exists")
    return APIResponse.success(role_data)

def update_role(role_id):
    role_data = request.get_json()
    role_service.update_role(role_data, role_id)
    return APIResponse.success()

def delete_role(role_id):
    role_service.delete_role(role_id)
    return APIResponse.success()