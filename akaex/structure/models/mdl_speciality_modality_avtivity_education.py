from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *
from structure.models.mdl_speciality_modality import SpecialityModality

class SpecialityModalityAvtivityEducation(BaseAkModel):
    """Represents the relationship between a speciality modality, an activity and an education"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    speciality = models.ForeignKey(SpecialityModality, on_delete=models.CASCADE, verbose_name=_('speciality'), db_column='id_especialidad')
    activity = models.ForeignKey(StructureActivityType, on_delete=models.CASCADE, verbose_name=_('activity'), db_column='id_actividad_estructura')
    #activity is now typification_education
    education_type = models.ForeignKey(EducationType, on_delete=models.CASCADE, verbose_name=_('education_type'), db_column='id_educacion')
    education_level_type = models.ForeignKey(EducationLevelType, on_delete=models.CASCADE, verbose_name=_('education_level_type'), db_column='id_nivel_educativo')
    class Meta:
        verbose_name = _('SpecialityModalityAvtivityEducation')
        verbose_name_plural = _('SpecialityModalityAvtivityEducations')
        db_table = f'{APP_LABEL.lower()}_tbr_especialidad_modalidad__actividad__educacion'

    def __str__(self):
        return f'{str(self.speciality)} - {str(self.activity)} - {str(self.education_type)} - {str(self.education_level_type)} '
