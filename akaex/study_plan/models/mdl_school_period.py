from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL


class SchoolPeriod(BaseAkModel):
    """Relates the school periods that will be part of the school frames"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('School period')
        verbose_name_plural = _('School periods')
        db_table = f'{APP_LABEL.lower()}_tbd_periodo_lectivo'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(SchoolPeriod)