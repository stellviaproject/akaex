from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType
from .mdl_branch import BranchType


class FamilyType(BaseType):
    branch = models.ForeignKey(BranchType, on_delete=models.SET_NULL, null=True, verbose_name=_('branch'),
                               db_column='id_rama')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'),
                                   db_column='descripcion')

    class Meta:
        verbose_name = _('FamilyType')
        verbose_name_plural = _('FamilyTypes')
        db_table = f'{APP_LABEL.lower()}_tbn_familia'
