from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import Template, TitleData, EndorserResponsibility


class TitleConfiguration(BaseAkModel):
    data = models.ManyToManyField(TitleData, through='DataTitleConfiguration', verbose_name=_('data'), db_column='dato')
    responsibility = models.ManyToManyField(EndorserResponsibility, through='EndorserResponsibilityTitleConfiguration', verbose_name=_('responsibility'), db_column='responsabilidad')
    template = models.ForeignKey(Template, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('template'), db_column='plantilla')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Title configuration')
        verbose_name_plural = _('Title Configurations')
        db_table = f'{APP_LABEL.lower()}_tbd_configuracion_titulo'

    def __str__(self):
        return f'{str(self.name)}'