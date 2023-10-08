from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class ResponsibilityType(BaseType):
    """
            Use it on structure/resonsability
    """

    class Meta:
        verbose_name = _('Responsibility')
        verbose_name_plural = _('Responsibilities')
        db_table = f'{APP_LABEL.lower()}_tbn_responsabilidad'
    #person_category_id = models.CharField(max_length=100, unique=False, null=True)
    #categoría_ocupacional = models.CharField(max_length=100, unique=True)
    #tipo_responsabilidad = models.CharField(max_length=100, unique=True, null=True)
   # nivel_preparacion = models.CharField(max_length=100, unique=True)
    #frente_aula = models.BooleanField(null=True, blank=True)

