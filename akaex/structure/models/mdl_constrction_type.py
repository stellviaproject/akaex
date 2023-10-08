from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL

class ConstructionType(BaseAkModel):
    """Represents the constructions"""
    description = models.CharField(max_length=250, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('ConstructionType')
        verbose_name_plural = _('ConstructionTypes')
        db_table = f'{APP_LABEL.lower()}_tbd_construccion'

    def __str__(self):
        return self.name