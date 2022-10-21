from umongo import Document, fields

from .authorization import Role


class User(Document):
    username = fields.StringField(unique=True)
    password = fields.StringField()
    groups = fields.ListField(fields.ReferenceField(Role))
    disabled = fields.BooleanField(default=False)