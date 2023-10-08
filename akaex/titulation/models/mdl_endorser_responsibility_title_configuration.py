from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import TitleConfiguration, EndorserResponsibility


class EndorserResponsibilityTitleConfiguration(BaseAkModel):
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'),db_column='nombre')
    responsibility = models.ForeignKey(EndorserResponsibility, on_delete=models.CASCADE, verbose_name=_('responsibility'), db_column='responsabilidad')
    title = models.ForeignKey(TitleConfiguration, on_delete=models.CASCADE,verbose_name=_('title_configuration'), db_column='titulo')


    class Meta:
        verbose_name = _('Endorser responsibility title configuration')
        verbose_name_plural = _('Endorser responsibility title configurations')
        db_table = f'{APP_LABEL.lower()}_tbr_responsabilidad_avaladora_configuracion_titulo'

    def __str__(self):
        return f'{str(self.title)} - {str(self.responsibility)}'