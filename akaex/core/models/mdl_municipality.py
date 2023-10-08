from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_province import Province


class Municipality(BaseAkModel):
    short_name = models.CharField(_('short name'), max_length=50, db_column='nombre_corto')
    code = models.CharField(_('code'), max_length=50, db_column='codigo')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')

    class Meta:
        verbose_name = _('Municipality')
        verbose_name_plural = _('Municipalities')
        ordering = ['code']
        db_table = f'{APP_LABEL.lower()}_tbn_municipio'
