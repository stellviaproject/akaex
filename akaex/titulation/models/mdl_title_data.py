from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL


class TitleData(BaseAkModel):
    variable = models.CharField(max_length=50, verbose_name=_('variable'), db_column='variable')
    data_type = models.BooleanField(verbose_name=_('data_type'), choices=[(True, 'Fijo'), (False, 'Variable')], default=None, db_column='tipo_dato')
    is_editable = models.BooleanField(verbose_name=_('is_editable'), choices=[(True, 'Editable'), (False, 'No editable')], default=None, db_column='editable')

    class Meta:
        verbose_name = _('Title data')
        verbose_name_plural = _('Title data')
        db_table = f'{APP_LABEL.lower()}_tbd_dato_titulo'

    def __str__(self):
        return f'{str(self.name)}'

