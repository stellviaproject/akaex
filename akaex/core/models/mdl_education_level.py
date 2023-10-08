from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class EducationLevelType(BaseType):
    """
            Use it on structure/configuration
    """
    orden = models.PositiveIntegerField(default=0, db_column='orden')

    class Meta:
        verbose_name = _('Education Level')
        verbose_name_plural = _('Education Levels')
        db_table = f'{APP_LABEL.lower()}_tbn_nivel_educativo'
