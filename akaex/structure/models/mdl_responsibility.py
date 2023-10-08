from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *

class Responsibility(BaseAkModel):
    """Represents the responsibilities"""
    occupational_category = models.ForeignKey(CategoryOcupationType, on_delete=models.SET_NULL, null=True, verbose_name=_('occupational_category'), db_column='id_categoria_ocupacional')
    description = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Responsibility')
        verbose_name_plural = _('Responsibilities')
        db_table = f'{APP_LABEL.lower()}_tbd_responsabilidad'

    def __str__(self):
        return self.name