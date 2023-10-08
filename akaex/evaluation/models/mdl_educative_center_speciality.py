from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from evaluation.nom_types import APP_LABEL

from core.models import EducationLevelType, EducationType, StructureActivityType
from structure.models import Structure, Speciality


class EducativeCenterSpeciality(BaseAkModel):
    """"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    educative_center = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('educative center'), db_column='centro educativo')
    educative_level = models.ForeignKey(EducationLevelType, on_delete=models.CASCADE, default=None, blank=True,verbose_name=_('educative_level'), db_column='nivel_educacion')
    education = models.ForeignKey(EducationType, on_delete=models.CASCADE, default=None, blank=True, verbose_name=_('education'), db_column='educacion')
    tipification = models.ForeignKey(StructureActivityType, on_delete=models.CASCADE, default=None, blank=True,verbose_name=_('tipification'), db_column='tipificacion')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, default=None, blank=True, verbose_name=_('speciality'), db_column='especialidad')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Educative center speciality')
        verbose_name_plural = _('Educative center specialities')
        db_table = f'{APP_LABEL.lower()}_tbr_centro_educativo_especialidad'

    def __str__(self):
        return f'{str(self.educative_center)}'
