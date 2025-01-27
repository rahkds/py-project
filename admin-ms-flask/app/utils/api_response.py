from flask import Response
from app.config import constants
import json
from app.utils.common import CustomJSONEncoder

class APIResponse:
    """
        A Utitily Class for generating consistent API response objects
    """

    @staticmethod
    def success(data=None, message = constants.SUCCESS_MESSAGE, status_code=constants.HTTP_OK):
        response = {
            "status" : True,
            "message" : message,
            "data" : data if data else {}
        }
        res_obj = Response(json.dumps(response,cls=CustomJSONEncoder), content_type='application/json')
        return res_obj, status_code
    
    @staticmethod
    def validation_error(errors=None, message=constants.VALIDATION_ERROR_MESSAGE, status_code=constants.HTTP_BAD_REQUEST):
        response = {
            "status" : False,
            "message" : message,
            "errors" : str(errors) if errors else {}
        }
        res_obj = Response(json.dumps(response, cls=CustomJSONEncoder), content_type='application/json')
        return res_obj, status_code
    
    @staticmethod
    def server_error(errors=None, message=constants.SERVER_ERROR_MESSAGE, status_code=constants.HTTP_INTERNAL_SERVER_ERROR):
        response = {
            "status" : False,
            "message" : message,
            "errors" : str(errors) if errors else {}
        }
        res_obj = Response(json.dumps(response, cls=CustomJSONEncoder), content_type='application/json')
        return res_obj, status_code
