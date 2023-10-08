from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_version import StudyPlanVersion
from .mdl_study_modality import StudyModality
from .mdl_course_type import CourseType

class StudyPlanConfiguration(BaseAkModel):
    """Represents the versions of the study plan in which modality and type of course they will be taught"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    study_plan_version = models.ForeignKey(StudyPlanVersion, on_delete=models.CASCADE, verbose_name=_('study plan version'), db_column='version_plan')
    study_modality = models.ForeignKey(StudyModality, on_delete=models.CASCADE, verbose_name=_('study modality'), db_column='modalidad')
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE, verbose_name=_('course type'), db_column='tipo_curso')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Study plan configuration')
        verbose_name_plural = _('Study plan configurations')
        db_table = f'{APP_LABEL.lower()}_tbd_configuracion_plan_estudio'

    def __str__(self):
        return f'{str(self.study_plan_version)} - {str(self.study_modality)} - {str(self.course_type)}'

auditlog.register(StudyPlanConfiguration)