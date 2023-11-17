from motor.motor_asyncio import AsyncIOMotorCollection

from src.core.db import db
from src.core.config.db import settings_db
from src.core.log import log


class FormRepozitory:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def find_one(self, query: dict):
        return await self.collection.find_one(query)

    async def find(self, query: dict = None, project: dict = None):
        project = project or {"_id": 0}
        try:
            return await self.collection.find(query, project).to_list(None)
        except Exception as e:
            log.error(e)

    async def aggregate(self, query_params: dict):
        query = [
            {
                '$project': {
                    'keys': {
                        '$map': {
                            'input': {'$objectToArray': "$$ROOT"},
                            'as': 'kv',
                            'in': {
                                '$cond': {
                                    'if': {'$ne': ['$$kv.k', '_id']},
                                    'then': '$$kv.k',
                                    'else': '$$REMOVE'
                                }
                            }
                        }
                    },
                    'document': "$$ROOT"
                }
            },
            {
                '$match': {
                    '$expr': {
                        '$eq': [
                            {'$size': {
                                '$setDifference': ['$keys.k', ['name', *list(query_params)]]
                            }}, 0
                        ]
                    }
                }
            },
            {
                '$project': {
                    'keys': 0,
                    '_id': 0,
                    'document._id': 0
                    }
            }
        ]

        try:
            res = await self.collection.aggregate(query).to_list(None)
            return [i['document'] for i in res]

        except Exception as e:
            log.error(e)


form_repozitory = FormRepozitory(db.get_collection(settings_db.MONGO_COLLECTION))
