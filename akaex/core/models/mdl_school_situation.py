from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class SchoolSituationType(BaseType):
    """
        Used in Procedure
    """
    name = models.CharField(max_length=50, unique=True, verbose_name=_('name'), db_column='nombre')
    # description = models.CharField(max_length=500, null=True, blank=True, default=None, unique=True, verbose_name=_('description'), db_column='descripcion')
    # type = models.CharField(max_length=50, null=True, blank=True, default=None)

    class Meta:
        verbose_name = _('School Situation')
        verbose_name_plural = _('School Situations')
        db_table = f'{APP_LABEL.lower()}_tbn_situacion_escolar'
