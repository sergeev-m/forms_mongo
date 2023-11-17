from fastapi import APIRouter

from src.forms.service import form_service as fs


router = APIRouter()

router.add_api_route('/get_form', fs.get_form, methods={'post'}, response_model=dict | str)
