from app.services import admin_service

def get_all():
    return admin_service.get_list()