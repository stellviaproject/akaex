from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_version import StudyPlanVersion
from .mdl_discipline import Discipline
from .mdl_evaluation_type import EvaluationType
from .mdl_evaluation_way import EvaluationWay
from .mdl_evaluation_category import EvaluationCategory
from .mdl_qualification_range import QualificationRange


class DisciplineEvaluation(BaseAkModel):
    """Relates the evaluations that are incorporated into the disciplines that are part of the study plan versions"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    study_plan_version = models.ForeignKey(StudyPlanVersion, on_delete=models.CASCADE, verbose_name=_('study plan version'), db_column='version')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name=_('discipline'), db_column='disciplina')
    evaluation_way = models.ForeignKey(EvaluationWay, null=True, on_delete=models.CASCADE, verbose_name=_('evaluation way'), db_column='via')
    evaluation_type = models.ForeignKey(EvaluationType, null=True, on_delete=models.CASCADE, verbose_name=_('evaluation type'), db_column='tipo_evaluacion')
    range = models.ForeignKey(QualificationRange, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('range'), db_column='rango')
    evaluation_category = models.ForeignKey(EvaluationCategory, null=True, on_delete=models.CASCADE, verbose_name=_('evaluation category'), db_column='categoria')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Discipline evaluation')
        verbose_name_plural = _('Discipline evaluations')
        db_table = f'{APP_LABEL.lower()}_tbd_evaluacion_disciplina'

    def __str__(self):
        return f'{str(self.discipline)} - {str(self.evaluation_way)}'

auditlog.register(DisciplineEvaluation)