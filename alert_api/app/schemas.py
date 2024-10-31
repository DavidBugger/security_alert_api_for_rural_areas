from marshmallow import Schema, fields, validate

class AlertSchema(Schema):
    description = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    timestamp = fields.DateTime(required=True)
