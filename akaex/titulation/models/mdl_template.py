from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import *


class Template(BaseAkModel):
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    type = models.CharField(max_length=100, null=True, blank=True, choices=TEMPLATE_TYPE, default=None, verbose_name=_('type'), db_column='tipo')

    class Meta:
        verbose_name = _('Template')
        verbose_name_plural = _('Templates')
        db_table = f'{APP_LABEL.lower()}_tbd_plantilla'

    def __str__(self):
        return f'{str(self.name)}'