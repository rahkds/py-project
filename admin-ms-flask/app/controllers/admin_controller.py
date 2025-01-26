from app.services import admin_service
from app.utils.api_response import APIResponse

def get_all():
    admin_data =  admin_service.get_list()
    return APIResponse.success(admin_data)