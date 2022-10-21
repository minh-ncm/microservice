import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from umongo.frameworks import MotorAsyncIOInstance


class MongoClient(object):
    @classmethod
    def get_engine(clazz, db_uri:str, db_name:str):
        client = AsyncIOMotorClient(db_uri)[db_name]
        client.get_io_loop = asyncio.get_running_loop
        engine = MotorAsyncIOInstance(client)
        return engine