from app.services import admin_service
from app.utils.api_response import APIResponse
from flask import request

def get_all():
    admin_data =  admin_service.get_list()
    return APIResponse.success(admin_data)

def create():
    admin_data = request.get_json()
    admin_exists = admin_service.check_admin_by_email(admin_data['email'])
    if admin_exists:
        return APIResponse.validation_error(message='admin already exists')
    admin_service.create_admin(admin_data)
    return APIResponse.success()