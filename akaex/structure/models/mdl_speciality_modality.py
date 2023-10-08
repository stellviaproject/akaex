from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *
from .mdl_speciality import Speciality

class SpecialityModality(BaseAkModel):
    """Represents the modalities of specialities"""
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True, default=None, verbose_name=_('speciality'), db_column='id_especialidad')

    speciality_type = models.ForeignKey(SpecialityType, on_delete=models.SET_NULL, null=True, verbose_name=_('speciality_type'), db_column='id_tipo_especialidad')
    code = models.CharField(max_length=50, unique=True, null=True, blank=True, default='', verbose_name=_('code'), db_column='codigo')
    family = models.ForeignKey(FamilyType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('family'), db_column='id_familia')
    branch = models.ForeignKey(BranchType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('branch'), db_column='id_rama')
    activity_education_level = models.ManyToManyField(StructureActivityType, through='SpecialityModalityAvtivityEducation', through_fields=["speciality", "activity"], verbose_name=_('activity_education_level'))

    class Meta:
        verbose_name = _('SpecialityModality')
        verbose_name_plural = _('SpecialityModalities')
        db_table = f'{APP_LABEL.lower()}_tbd_modalidad_especialidad'

    def __str__(self):
        return f'{str(self.speciality)}'