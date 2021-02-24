from datetime import datetime

from rest_framework.exceptions import ValidationError


def year_validator(value):
    if value > datetime.now().year:
        raise ValidationError(
            f'year={value} - год создания произведения не может превышать '
            f'текущий'
        )