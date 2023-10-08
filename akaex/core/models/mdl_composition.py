from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class CompositionType(BaseType):
    """
            Use it on structure/configuration
    """

    class Meta:
        verbose_name = _('Composition')
        verbose_name_plural = _('Compositions')
        db_table = f'{APP_LABEL.lower()}_tbn_composicion'
