from marshmallow import Schema, fields, validate
from app.utils.common import CommonUtil

class CreateAdminSchema(Schema):
    email = fields.Email(required=True, validate=CommonUtil().not_empty)
    username = fields.Str(required=True, validate=CommonUtil().not_empty)
    login_type = fields.Str(validate=validate.OneOf(['Email','Facebook','Google+','Phone Number']))
    status = fields.Integer(required=True, validate=validate.OneOf([0,1]))
    # Mobile = fields.Str(validate=validate.Regexp(r'/^(\+\d{1,3}[- ]?)?\d{10}$/'))