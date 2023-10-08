from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_evaluation_type import EvaluationType
from .mdl_evaluation_way import EvaluationWay


class EvaluationWayType(BaseAkModel):
    """Relates evaluation ways with evaluation types"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    evaluation_type = models.ForeignKey(EvaluationType, on_delete=models.CASCADE, verbose_name=_('evaluation type'), db_column='tipo_evaluacion')
    evaluation_way = models.ForeignKey(EvaluationWay, on_delete=models.CASCADE, verbose_name=_('evaluation way'), db_column='via_evaluacion')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Evaluation way type')
        verbose_name_plural = _('Evaluation way types')
        db_table = f'{APP_LABEL.lower()}_tbr_via_tipo_evaluacion'

    def __str__(self):
        return f'{str(self.evaluation_type)} : {str(self.evaluation_way)}'

auditlog.register(EvaluationWayType)