from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType
from .mdl_education_level import EducationLevelType


class EducationType(BaseType):
    color = ColorField(default='#FFFFFF')
    education_levels = models.ManyToManyField(EducationLevelType, through='EducationTypeEducationLevelType', related_name='education_levels')
    obligatory = models.BooleanField(default=False, verbose_name=_('obligatory'), db_column='obligatorio')

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')
        db_table = f'{APP_LABEL.lower()}_tbn_educacion'
