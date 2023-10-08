from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *
from .mdl_characteristics import Characteristics


class CharacteristicValue(BaseAkModel):
    """Represents the value of the characteristics"""
    characteristic = models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=True, verbose_name=_('characteristic'), db_column='id_caracteristica')
    value = models.IntegerField(verbose_name=_('value'), db_column='valor')

    class Meta:
        verbose_name = _('Characteristic_value')
        verbose_name_plural = _('Characteristic_values')
        db_table = f'{APP_LABEL.lower()}_tbd_caracteristica__valor_caracteristica'

    def __str__(self):
        return f'{str(self.characteristic)} - {str(self.value)}'