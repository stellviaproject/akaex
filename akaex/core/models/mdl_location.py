from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType
from .mdl_province import Province
from .mdl_municipality import Municipality


class LocationType(BaseType):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('municipality'), db_column='id_municipio')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'),db_column='descripcion')

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
        db_table = f'{APP_LABEL.lower()}_tbn_localidad'

