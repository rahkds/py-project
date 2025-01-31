from marshmallow import Schema, fields, validate, validates, ValidationError, pre_load
from app.utils.common import CommonUtil

class CreateRoleSchema(Schema):
    role_name = fields.Str(required=True, validate=CommonUtil().not_empty)
    description = fields.Str(required=True)
    status = fields.Integer(required=True,validate=validate.OneOf([0,1]))

class UpdateRoleSchema(Schema):
    role_name = fields.Str(validate=CommonUtil().not_empty)
    description = fields.Str()
    status = fields.Integer(validate=validate.OneOf([0,1]))

    @pre_load
    def forbidden_field_check(self, data, **kwargs):
        forbidden_fields = ['_id']
        for key in forbidden_fields:
            if key in data:
                raise ValidationError(f"Forbidden_field: {key}")
        return data