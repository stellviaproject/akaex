from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL

class EndorserResponsibility(BaseAkModel):
    """Represents the responsibilities that will be associated with the people who sign the titles or certificates"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Endorser responsibility')
        verbose_name_plural = _('Endorser responsibilities')
        db_table = f'{APP_LABEL.lower()}_tbn_responsabilidad_avaladora'

    def __str__(self):
        return f'{str(self.name)}'