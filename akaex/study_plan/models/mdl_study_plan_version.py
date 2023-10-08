from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan import StudyPlan
from .mdl_subject import Subject
from .mdl_discipline import Discipline
from .mdl_evaluation_way import EvaluationWay


class StudyPlanVersion(BaseAkModel):
    """Collect the versions that a study plan may have"""
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, verbose_name=_('study plan'), db_column='plan_estudio')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    discipline_subject = models.ManyToManyField(Subject, through='SubjectVersionPlan', through_fields=['study_plan_version', 'subject'], verbose_name=_('subjects'), db_column='asignatura')
    discipline_evaluation = models.ManyToManyField(Discipline, default=None, blank=True, through='DisciplineEvaluation', through_fields=['study_plan_version', 'discipline'], verbose_name=_('discipline evaluation'), db_column='evaluacion_disciplina')
    evaluation_culmination = models.ManyToManyField(EvaluationWay, default=None, blank=True, through='EvaluationCulminationStudy', through_fields=['study_plan_version', 'evaluation_way'], verbose_name=_('evaluation culmination'), db_column='evaluacion_culminacion_estudio')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Study plan version')
        verbose_name_plural = _('Study plan versions')
        db_table = f'{APP_LABEL.lower()}_tbd_version_plan_estudio'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(StudyPlanVersion)