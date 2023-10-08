from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_school_frame import SchoolFrame
from .mdl_study_plan_version import StudyPlanVersion
from .mdl_subject import Subject
from .mdl_evaluation_culmination_study import EvaluationCulminationStudy


class StudyPlanOrganization(BaseAkModel):
    """Relates the organizations that can be given to the different study plans"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    school_frame = models.ForeignKey(SchoolFrame, on_delete=models.CASCADE, verbose_name=_('school frame'), db_column='marco')
    study_plan_version = models.ForeignKey(StudyPlanVersion, on_delete=models.CASCADE, verbose_name=_('version_plan'))
    resolution = models.CharField(max_length=255, default=None, null=True, blank=True, verbose_name=_('resolution'), db_column='resolucion')
    subject_organization = models.ManyToManyField(Subject, through='SubjectOrganization', through_fields=['study_plan_organization', 'subject'], default=None, blank=True, verbose_name=_('subject organization'), db_column='organizacion asignatura')
    evaluation = models.ManyToManyField(EvaluationCulminationStudy, through='StudyPlanOrganizationEvaluation', through_fields=['study_plan_organization', 'evaluation_culmination_study'], default=None, verbose_name=_('evaluation'), db_column='evaluacion')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Study plan organization')
        verbose_name_plural = _('Study plan organizations')
        db_table = f'{APP_LABEL.lower()}_tbd_organizacion_plan_estudio'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(StudyPlanOrganization)