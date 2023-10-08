from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import Endorser, TitleConfiguration, Title


class TitleEndorser(BaseAkModel):
    endorser = models.ForeignKey(Endorser, default=None, null=True, blank=True,  on_delete=models.CASCADE, verbose_name=_('endorser'), db_column='avalador')
    title = models.ForeignKey(Title, on_delete=models.CASCADE, verbose_name=_('title'), db_column='titulo')
    #configuration_title= models.ForeignKey(TitleConfiguration, on_delete=models.CASCADE, verbose_name=_('configuration_title'), db_column='configuration_titulo')

    class Meta:
        verbose_name = _('Title Endorser')
        verbose_name_plural = _('Title Endorsers')
        db_table = f'{APP_LABEL.lower()}_tbr_avalador_titulo'

    def __str__(self):
        return f'{str(self.endorser)} - {str(self.title)} - '
