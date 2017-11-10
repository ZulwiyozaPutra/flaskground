from datetime import date
from marshmallow import Schema, fields


class Model(object):
    def __init__(self):
        self.created_at = date.now()
        self.modified_at = date.now()


class ModelSchema(Schema):
    created_at = fields.Date()
    modified_at = fields.Date()
