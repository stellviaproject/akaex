from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL


class EvaluationType(BaseType):
    """Relates the types (frequency) of evaluations that exists"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Evaluation type')
        verbose_name_plural = _('Evaluation types')
        db_table = f'{APP_LABEL.lower()}_tbd_tipo_evaluacion'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(EvaluationType)