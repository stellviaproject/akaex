from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from structure.models import SpecialityModalityAvtivityEducation
from study_plan.nom_types import APP_LABEL

from .mdl_study_plan_configuration import StudyPlanConfiguration


class SpecialityStudyPlanConfiguration(BaseAkModel):
    """Relates a study plan configuration with a speciality configuration"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    study_plan_configuration = models.ManyToManyField(StudyPlanConfiguration, verbose_name=_('study plan configuration'), db_column='configuracion_plan')
    speciality_configuration = models.ForeignKey(SpecialityModalityAvtivityEducation, on_delete=models.CASCADE, verbose_name=_('specialties'), db_column='configuracion_especialidad')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Speciality study plan configuration')
        verbose_name_plural = _('Speciality study plan configurations')
        db_table = f'{APP_LABEL.lower()}_tbr_especialidad_configuracion_plan_estudio'

    def __str__(self):
        return f'Configuration - {str(self.speciality_configuration)}'

auditlog.register(SpecialityStudyPlanConfiguration)