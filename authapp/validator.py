
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_age(value):
    if value < 0:
        raise ValidationError(
            _(f'Возраст не может быть отрицательным'),
            params={'value': value}
        )