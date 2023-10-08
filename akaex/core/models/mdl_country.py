from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class CountryType(BaseType):
    """
            Use it on structure/configuration
    """
    name_es = models.CharField(_('name_es'),max_length=100, default='', db_column='nombre_es')
    name_en = models.CharField(_('name_en'),max_length=100, default='', db_column='nombre_en')
    iso2 = models.CharField(max_length=2, default='', verbose_name=_('iso2'))
    iso3 = models.CharField(max_length=3, default='', verbose_name=_('iso3'))
    phone_code = models.IntegerField(default=0, verbose_name=_('phone code'), db_column='codigo_telefonico')
    capital = models.CharField(null=True, max_length=100, blank=True, verbose_name=_('capital'), db_column='capital')
    demonym = models.CharField(null=True, max_length=100, blank=True, verbose_name=_('demonym'), db_column='gentilicio')
    icon_flat = models.ImageField(null=True, blank=True, verbose_name=_('icon flat'), db_column='icono')

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        db_table = f'{APP_LABEL.lower()}_tbn_pais'

