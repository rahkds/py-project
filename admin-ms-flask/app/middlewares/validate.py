from marshmallow import Schema
from flask import request
from app.utils.api_response import APIResponse

def validate_request_schema(schema: Schema):
    """
        A decorator to validate request body or query fields
        :param schema: marshmallow Schema created for request
    """
    def decorator(f):
        def decorated_function(*args, **kwargs):
           request_data = request.args.to_dict(flat=False)
           if request.method in ['POST', 'PUT']:
               request_data = request.get_json()
           try:
               schema().load(request_data, unknown='exclude')
           except Exception as e:
               return APIResponse.validation_error(e)
           
           return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator
