from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_nom_type import NomType


class Nomenclator(BaseAkModel):
    type = models.CharField(max_length=100, verbose_name=_('type'), db_column='tipo')
    nom_type = models.ForeignKey(NomType, on_delete=models.CASCADE,  verbose_name=_('nom type'), db_column='nomenclador')

    class Meta:
        verbose_name = _('Nomenclator')
        verbose_name_plural = _('Nomenclators')
        indexes = [
            models.Index(fields=['name', 'type']),
        ]
        db_table = f'{APP_LABEL.lower()}_tbn_nomenclador'

    def __str__(self):
        return f'{self.type} ({self.name})'

