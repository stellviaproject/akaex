from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_version import StudyPlanVersion
from .mdl_subject_type import SubjectType


class NotLectiveSubject(BaseAkModel):
    """Relates the amounts of non-lective subjects that are associated with a version of the study plan"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    study_plan_version = models.ForeignKey(StudyPlanVersion, on_delete=models.CASCADE, verbose_name=_('study plan version'), db_column='version_plan')
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE, verbose_name=_('subject type'), db_column='tipo_asignatura')
    amount = models.IntegerField(verbose_name=_('amount'), db_column='cantidad')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Not lective subject')
        verbose_name_plural = _('Not lective subjects')
        db_table = f'{APP_LABEL.lower()}_tbd_asignatura_no_lectiva'

    def __str__(self):
        return f' {str(self.study_plan_version)} - {str(self.subject_type)}'

auditlog.register(NotLectiveSubject)