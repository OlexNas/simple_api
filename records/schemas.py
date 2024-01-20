from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class TickerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    user_id = fields.Int()

