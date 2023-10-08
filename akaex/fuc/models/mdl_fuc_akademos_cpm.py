from datetime import datetime
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from fuc.nom_types import APP_LABEL, CONST_CPM_NOM_TYPE_CHOICES


class FUCAkademosCPM(BaseAkModel):
    fuc_id = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('fuc id'), db_column='fuc_id')
    id_akademos = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('id_akademos'), db_column='id_akademos')
    nom_type = models.CharField(max_length=255, blank=True, null=True, choices=CONST_CPM_NOM_TYPE_CHOICES, verbose_name=_('nom type'), db_column='tipo_nom')

    class Meta:
        verbose_name = _('FUC Akademos CPM')
        verbose_name_plural = _('FUC Akademos CPM')
        db_table = f'{APP_LABEL.lower()}_tbn_akademos_cpm'

        def __str__(self):
            return f'{str(self.fuc_id)}-{nom_type}'
