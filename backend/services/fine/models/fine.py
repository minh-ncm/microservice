from umongo import Document, fields

from .. import constants
from backend.commons.databases import MongoClient
from backend.services.fine.env import env


instance = MongoClient.get_engine(env.MONGO_URI_FINE, env.MONGO_DB_NAME_FINE)


@instance.register
class Fine(Document):
    user_id = fields.ObjectIdField()
    amount = fields.IntegerField()
    desc = fields.StringField()
    status = fields.IntegerField(default=constants.FINE_STATUS_UNPAID)
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()