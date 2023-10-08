from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType
from .mdl_organism import OrganismType


class EducationalCenterType(BaseType):
    """
            Use it on structure/configuration
    """
    color = ColorField(default='#FFFFFF')
    short_name = models.CharField(_('short_name'), max_length=50, db_column='nombre_corto')
    organism = models.ForeignKey(OrganismType, on_delete=models.SET_NULL, null=True, verbose_name=_('organism'), db_column='id_organismo')

    class Meta:
        verbose_name = _('Educational Center')
        verbose_name_plural = _('Educational Centers')
        db_table = f'{APP_LABEL.lower()}_tbn_centro_educacional'

