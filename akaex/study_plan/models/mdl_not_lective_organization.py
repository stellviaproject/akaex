from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_organization import StudyPlanOrganization
from .mdl_not_lective_subject import NotLectiveSubject
from .mdl_academic_year import AcademicYear
from .mdl_school_period import SchoolPeriod


class NotLectiveOrganization(BaseAkModel):
    """Relates the organization (school period, academic year, etc.) that is associated with the non-lective subjects defined for the study plan version"""
    study_plan_organization = models.ForeignKey(StudyPlanOrganization, on_delete=models.CASCADE, verbose_name=_('study plan organization'), db_column='organizacion')
    not_lective_subject = models.ForeignKey(NotLectiveSubject, on_delete=models.CASCADE, verbose_name=_('not lective subject'), db_column='asignatura')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name=_('academic year'), db_column='año')
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, verbose_name=_('school period'), db_column='periodo')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Not lective organization')
        verbose_name_plural = _('Not lective organizations')
        db_table = f'{APP_LABEL.lower()}_tbd_organizacion_no_lectiva'

    def __str__(self):
        return f'{str(self.study_plan_organization)} - {str(self.not_lective_subject)}'

auditlog.register(NotLectiveOrganization)