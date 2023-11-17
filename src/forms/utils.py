from src.forms.validators import is_date, is_phone, is_email


class CheckTypes:
    __exclude_fields = ('name',)
    __validators = (is_date, is_phone, is_email)

    def __call__(self, data: dict | list[dict]):
        if isinstance(data, list):
            return [self.__validate(row) for row in data]
        return self.__validate(data)

    def __validate(self, __input_value: dict) -> dict:
        return {field: self.get_type(field, value) for field, value in __input_value.items()}

    def get_type(self, field, value: str):
        if field in self.__exclude_fields:
            return value
        for validate in self.__validators:
            try:
                return validate(value)
            except ValueError:
                continue
        return 'text'


format_type = CheckTypes()
