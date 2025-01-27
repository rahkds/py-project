from marshmallow import Schema, fields, validate, validates, ValidationError, pre_load
from app.utils.common import CommonUtil
from bson import ObjectId



class CreateAdminSchema(Schema):
    email = fields.Email(required=True, validate=CommonUtil().not_empty)
    username = fields.Str(required=True, validate=CommonUtil().not_empty)
    login_type = fields.Str(validate=validate.OneOf(['Email','Facebook','Google+','Phone Number']))
    status = fields.Integer(required=True, validate=validate.OneOf([0,1]))
    # Mobile = fields.Str(validate=validate.Regexp(r'/^(\+\d{1,3}[- ]?)?\d{10}$/'))

class UpdateAdminSchema(Schema):
    email = fields.Email(validate=CommonUtil().not_empty)
    username = fields.Str(validate=CommonUtil().not_empty)
    login_type = fields.Str(validate=validate.OneOf(['Email','Facebook','Google+','Phone Number']))
    status = fields.Integer(validate=validate.OneOf([0,1]))

    @pre_load
    def forbidden_fields(self, data, **kwargs):
        forbidden_fields = ['_id']
        for key in forbidden_fields:
            if key in data:
                raise ValidationError(f"Forbidden_field: {key}")
        return data

    # @validates('_id')
    # def validate_user_id(self, value):
    #     try:
    #         ObjectId(value)
    #     except Exception:
    #         raise ValidationError(f"Invalid ObjectId: {value}")