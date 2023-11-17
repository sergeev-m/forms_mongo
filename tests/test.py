import copy
import asyncio
import requests

from src.core.config.db import settings_db
from src.core.log import log
from src.core.db import db, client
from src.core.config.settings import settings
from src.forms.service import form_service


async def test(item: dict, query=None, any_q=''):
    item.pop('name')
    query = query or "&".join([f"{k}={v}" for k, v in item.items()])
    url = f'{settings.TEST_URL}?{query}{any_q}'
    res = requests.post(url)
    print(f'Request {url}\nResponse: {res.json()}\n')


async def perform_test_queries():
    documents = await form_service.get_all()

    try:
        log.debug("Все документы в коллекции:")
        for document in documents:
            print(document, '\n')

        log.debug('Запросы, возвращающие название формы:')
        for item in copy.deepcopy(documents):
            await test(item)

        log.debug('Запросы без совпадений:\n\n')
        for item in copy.deepcopy(documents):
            item.popitem()
            query = "&".join([f"no_match_field={v}" for k, v in item.items()])
            await test(item=item, query=query)

        log.debug('Запросы с лишним полем\n\n')
        for item in copy.deepcopy(documents):
            field = '&лишнее поле=лишнее'
            await test(item=item, any_q=field)

    except Exception as e:
        log.error(str(e))

    client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(perform_test_queries())
