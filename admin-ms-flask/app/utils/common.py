import json
from bson import ObjectId
from datetime import datetime

class CommonUtil():
    """
        CommonUtil - singleton class
        contains various common utitilty methods
    """
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def is_empty(self, value):
        if value is None:
            return True
        if isinstance(value, (str, list, tuple, set, dict)):
            return len(value) == 0
        if isinstance(value, (int, float)) and value == 0:
            return True
        return False
    
    def not_empty(self, value):
        return not self.is_empty(value)


# Custom JSON encoder to handle ObjectId and datetime
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


