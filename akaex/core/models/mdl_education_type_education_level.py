from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL
from .mdl_education import EducationType
from .mdl_education_level import EducationLevelType


class EducationTypeEducationLevelType(BaseAkModel):
    education = models.ForeignKey(EducationType, on_delete=models.CASCADE, verbose_name=_('Education'), db_column='id_educacion')
    education_level = models.ForeignKey(EducationLevelType, on_delete=models.CASCADE, verbose_name=_('Education Level'), db_column='id_nivel_educativo')

    class Meta:
        verbose_name = _('education_level')
        db_table = f'{APP_LABEL.lower()}_tbr_educacion__nivel_educativo'