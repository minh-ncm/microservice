from umongo import Document, fields


class Permission(Document):
    code = fields.StringField(unique=True)
    desc = fields.StringField()


class Role(Document):
    code = fields.StringField(unique=True)
    desc = fields.StringField()
    permission_list = fields.ListField(fields.ReferenceField(Permission))