from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType
from .mdl_location import LocationType
from .mdl_province import Province
from .mdl_municipality import Municipality


class PopularCouncilType(BaseType):
    postal_code = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[0-9]+$')], verbose_name=_('postal_code'), db_column='codigo_postal')
    population = models.IntegerField(null=True, verbose_name=_('population'), db_column='no_poblacion')
    location = models.ForeignKey(LocationType, on_delete=models.SET_NULL, null=True, verbose_name=_('location'), db_column='id_localidad')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('province'), db_column='id_provincia')
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('municipality'), db_column='id_municipio')

    class Meta:
        verbose_name = _('Popular Council')
        verbose_name_plural = _('Popular Councils')
        db_table = f'{APP_LABEL.lower()}_tbn_consejor_popular'
