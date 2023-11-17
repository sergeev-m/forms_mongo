from fastapi import APIRouter

from src.forms.router import router as form_router


v1 = APIRouter()

v1.include_router(form_router, tags=['Form'])
v1.add_api_route('/', lambda: sorted({route.path for route in vars(v1)['routes']}))
