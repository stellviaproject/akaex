from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_version import StudyPlanVersion
from .mdl_discipline import Discipline
from .mdl_subject import Subject


class SubjectVersionPlan(BaseAkModel):
    """Represents the subjects that are grouped into disciplines within a version of the study plan"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    study_plan_version = models.ForeignKey(StudyPlanVersion, on_delete=models.CASCADE, verbose_name=_('study plan version'), default='', db_column='version_plan')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name=_('discipline'), db_column='disciplina')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('subject'), db_column='asignatura')
    school_hours = models.IntegerField(unique=False, null=False, verbose_name=_('school hours'), db_column='hora_clase')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Subject version plan')
        verbose_name_plural = _('Subject version plans')
        db_table = f'{APP_LABEL.lower()}_tbr_asignatura_version_plan'

    def __str__(self):
        return f'{str(self.discipline)} - {str(self.subject)}'

auditlog.register(SubjectVersionPlan)