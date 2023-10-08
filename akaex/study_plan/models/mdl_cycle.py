from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL


class Cycle(BaseAkModel):
    """Relate the cycles that will be part of the school frames, in which the academic years will be grouped"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
#    order = models.IntegerField(unique=True, null=False, verbose_name=_('order'), db_column='orden')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Cycle')
        verbose_name_plural = _('Cycles')
        db_table = f'{APP_LABEL.lower()}_tbd_ciclo'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(Cycle)