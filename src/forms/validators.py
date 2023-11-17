import re
from datetime import datetime

from pydantic import validate_email


def is_email(value: str):
    validate_email(value)
    return 'email'


def is_phone(value: str):
    value = value.replace(' ', '')
    phone_pattern = re.compile(r'^\+*7\d{10}$')
    if not phone_pattern.match(value):
        raise ValueError
    return 'phone'


def is_date(date: str):
    for format_date in ['%d.%m.%Y', '%Y-%m-%d']:
        try:
            datetime.strptime(date, format_date)
            return 'date'
        except ValueError:
            pass
    raise ValueError
