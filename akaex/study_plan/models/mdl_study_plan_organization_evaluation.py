from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_organization import StudyPlanOrganization
from .mdl_evaluation_culmination_study import EvaluationCulminationStudy


class StudyPlanOrganizationEvaluation(BaseAkModel):
    """Relates the organizations that can be given to the different study plans"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    study_plan_organization = models.ForeignKey(StudyPlanOrganization, on_delete=models.CASCADE, verbose_name=_('study plan organization'), db_column='organizacion plan estudio')
    evaluation_culmination_study = models.ForeignKey(EvaluationCulminationStudy, on_delete=models.CASCADE, verbose_name=_('evaulacion culminacion estudio'))

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Study plan organization evaluation')
        verbose_name_plural = _('Study plan organization evaluations')
        db_table = f'{APP_LABEL.lower()}_tbd_evaluacion_organizacion_plan_estudio'

    def __str__(self):
        return f'{str(self.study_plan_organization)}'

auditlog.register(StudyPlanOrganizationEvaluation)