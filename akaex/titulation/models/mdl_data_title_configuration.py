from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import TitleData, TitleConfiguration


class DataTitleConfiguration(BaseAkModel):
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'),db_column='nombre')
    data = models.ForeignKey(TitleData, on_delete=models.CASCADE, verbose_name=_('data'), db_column='dato')
    title_configuration = models.ForeignKey(TitleConfiguration, on_delete=models.CASCADE,verbose_name=_('title_configuration'), db_column='configuracion_titulo')

    class Meta:
        verbose_name = _('Data title configuration')
        verbose_name_plural = _('Data title configurations')
        db_table = f'{APP_LABEL.lower()}_tbr_dato_configuracion_titulo'

    def __str__(self):
        return f'{str(self.data)} - {str(self.title_configuration)}'