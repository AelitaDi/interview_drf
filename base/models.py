from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}
MinZeroValid = MinValueValidator(Decimal('0.00'))


class BaseModel(models.Model):
    """Base model."""
    objects = None
    created = models.DateTimeField('created at', auto_now_add=True)
    updated = models.DateTimeField('updated at', auto_now=True)

    class Meta:
        abstract = True


class LowerCaseEmailField(models.EmailField):
    """Email in lowercase."""

    def get_prep_value(self, value: str) -> str | None:
        if value:
            return str(value).lower()


class LowerCaseUsernameField(models.CharField):
    """Username in lowercase."""

    def get_prep_value(self, value: str) -> str | None:
        if value:
            return str(value).lower()
