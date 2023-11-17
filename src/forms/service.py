from fastapi import Request

from src.forms.repozitory import form_repozitory, FormRepozitory
from src.forms.utils import format_type


class FormService:
    def __init__(self, repozitory: FormRepozitory):
        self.repozitory = repozitory

    async def get_all(self):
        return await self.repozitory.find()

    async def get_form(self, req: Request) -> dict:
        query_params = format_type(dict(req.query_params))
        res = format_type(await self.repozitory.aggregate(query_params))

        for item in res:
            name = item.pop('name')
            if item.items() & query_params.items() == item.items():
                return name

        return query_params


form_service = FormService(form_repozitory)
