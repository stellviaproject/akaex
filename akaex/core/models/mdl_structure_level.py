from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType
from .mdl_structure_category import StructureCategoryType


class StructureLevelType(BaseType):
    """
            Used in Structure
    """
    category = models.ManyToManyField(StructureCategoryType, blank=True, default=None, verbose_name=_('category'), db_column='id_categoria_estructura')

    class Meta:
        verbose_name = _('Structure Level')
        verbose_name_plural = _('Structure Levels')
        db_table = f'{APP_LABEL.lower()}_tbn_nivel_estructura'


def get_default_level_pk():
    levels = StructureLevelType.objects.get_or_create(
        name='Nacional')
    levels = StructureLevelType.objects.first()
    if levels is None:
        data={
             "name": "Nacional",
             "is_disable": False
        }
        levels=StructureLevelType.objects.create(**data)
    return levels.pk
