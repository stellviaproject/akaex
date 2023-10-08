from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from colorfield.fields import ColorField
from study_plan.nom_types import APP_LABEL


class SubjectType(BaseAkModel):
    """Represents the types of subjects"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    color = ColorField(default='#FFFFFF', verbose_name=_('color'), db_column='color')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Subject type')
        verbose_name_plural = _('Subject types')
        db_table = f'{APP_LABEL.lower()}_tbd_tipo_asignatura'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(SubjectType)