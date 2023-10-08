from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_evaluation_type import EvaluationType


class EvaluationWay(BaseAkModel):
    """Relates the evaluation ways (instrument) that exists and that are grouped into the evaluation types"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    acronym = models.CharField(max_length=20, default=None, null=True, blank=True, verbose_name=_('acronym'), db_column='siglas')
    evaluation_type = models.ManyToManyField(EvaluationType, through='EvaluationWayType', verbose_name=_('evaluation type'), db_column='tipo_evaluacion')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Evaluation way')
        verbose_name_plural = _('Evaluation ways')
        db_table = f'{APP_LABEL.lower()}_tbd_via_evaluacion'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(EvaluationWay)