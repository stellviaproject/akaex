from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL


class NomType(BaseAkModel):
    type = models.CharField(_('type'), max_length=100, db_column='tipo')

    class Meta:
        verbose_name = _('Nom Type')
        verbose_name_plural = _('Nom Types')
        indexes = [
            models.Index(fields=['name', 'type']),
        ]
        db_table = f'{APP_LABEL.lower()}_tbn_tipo'

    def __str__(self):
        return f'{self.type} ({self.name})'
