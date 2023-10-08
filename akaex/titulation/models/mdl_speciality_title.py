from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import TitleConfiguration
from structure.models import SpecialityModalityAvtivityEducation


class SpecialityTitle(BaseAkModel):
    speciality = models.ForeignKey(SpecialityModalityAvtivityEducation, on_delete=models.CASCADE, verbose_name=_('speciality'), db_column='especialidad')
    title = models.ForeignKey(TitleConfiguration, on_delete=models.CASCADE, verbose_name=_('title'), db_column='configuracion_titulo')

    class Meta:
        verbose_name = _('Speciality title')
        verbose_name_plural = _('Speciality titles')
        db_table = f'{APP_LABEL.lower()}_tbr_titulo_especialidad'

    def __str__(self):
        return f'{str(self.title)} - {str(self.speciality)}'
