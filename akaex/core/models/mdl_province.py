from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL


class Province(BaseAkModel):
    short_name = models.CharField(_('short name'), max_length=50, db_column='nombre_corto')
    code = models.CharField(_('code'), max_length=50, db_column='codigo')

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')
        ordering = ['code']
        db_table = f'{APP_LABEL.lower()}_tbn_provincia'

