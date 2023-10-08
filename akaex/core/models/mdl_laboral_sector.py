from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class LaboralSectorType(BaseType):
    """
        Used in Procedure
    """

    class Meta:
        verbose_name = _('Laboral Sector')
        verbose_name_plural = _('Laboral Sectors')
        db_table = f'{APP_LABEL.lower()}_tbn_sector_laboral'
