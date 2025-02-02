from marshmallow import Schema
from flask import request
from app.utils.api_response import APIResponse

def validate_request_schema(bodySchema: Schema = None, queryParamSchema:Schema = None, **vkwargs):
    """
        A decorator to validate request body or query fields
        :param schema: marshmallow Schema created for request
    """
    def decorator(f):
        def decorated_function(*args, **kwargs):
            try:
                unknown_flag = "exclude"
                if "unknown" in vkwargs:
                     unknown_flag = vkwargs.get("unknown")

                if queryParamSchema:
                    request_data = request.args.to_dict(flat=False)
                    queryParamSchema().load(request_data, unknown=unknown_flag)

                if bodySchema:
                    request_data = request.get_json()
                    bodySchema().load(request_data, unknown=unknown_flag)
            except Exception as e:
                    return APIResponse.validation_error(e)
                      
            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator
