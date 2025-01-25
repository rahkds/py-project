from marshmallow import Schema, fields, ValidationError
from app.utils.common import CommonUtil

class EnvSchema(Schema):
    MONGO_USER = fields.Str(required=True)
    MONGO_HOST = fields.Str(required=True,validate=CommonUtil().not_empty)
    MONGO_PORT = fields.Int(required=True,validate=CommonUtil().not_empty)
    MONGO_DBNAME = fields.Str(required=True,validate=CommonUtil().not_empty)

