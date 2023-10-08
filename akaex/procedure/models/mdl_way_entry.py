from core.models import BaseType
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL


class WayEntry(BaseType):
    name = models.CharField(max_length=100, default="Way of entry", verbose_name=_('name'))
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Way of Entry')
        verbose_name_plural = _('Way of Entries')
        db_table = f'{APP_LABEL.lower()}_tbd_via_ingreso'

    def __str__(self):
        return self.name
