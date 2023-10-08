from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_teaching_level import TeachingLevel


class SpecialCapacity(BaseAkModel):
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    teaching_level = models.ForeignKey(TeachingLevel, on_delete=models.CASCADE, verbose_name=_('teaching level'), db_column='nivel_enseñanza')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Special capacity')
        verbose_name_plural = _('Special capacities')
        db_table = f'{APP_LABEL.lower()}_tbd_capacidad_especial'

auditlog.register(SpecialCapacity)