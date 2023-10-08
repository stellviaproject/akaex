from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_organization import StudyPlanOrganization
from .mdl_subject import Subject
from .mdl_subject_version import SubjectVersion
from .mdl_subject_type import SubjectType
from .mdl_discipline import Discipline
from .mdl_academic_year import AcademicYear
from .mdl_school_period import SchoolPeriod


class SubjectOrganization(BaseAkModel):
    """Relates the different organizations that can be given to the versions of lective subjects within the study plan"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    study_plan_organization = models.ForeignKey(StudyPlanOrganization, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('study plan organization'), db_column='organizacion_plan')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('subject'), db_column='asignatura')
    subject_version = models.ForeignKey(SubjectVersion, on_delete=models.CASCADE, verbose_name=_('subject version'), db_column='version_asignatura')
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE, verbose_name=_('subject type'), db_column='tipo_asignatura')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name=_('discipline'), db_column='disciplina')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name=_('academic year'), db_column='año')
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, verbose_name=_('school period'), db_column='periodo_lectivo')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Subject organization')
        verbose_name_plural = _('Subject organizations')
        db_table = f'{APP_LABEL.lower()}_tbd_organizacion_asignatura'

    def __str__(self):
        return f'{str(self.study_plan_organization)} - {str(self.subject_version)}'

auditlog.register(SubjectOrganization)