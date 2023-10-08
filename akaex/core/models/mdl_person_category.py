from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from core.generics.generic import BaseAkModel
from django.db.models.signals import pre_save, post_delete
from django.db import models, IntegrityError
from django.db.models import F
from django.core.validators import RegexValidator
from core.nom_types import PERSON_CATEGORY_TYPE

from core.utils import APP_LABEL

from .mdl_base_type import BaseType


class PersonCategoryType(BaseType):
    """
            Used in Person
    """
    priority= models.IntegerField(null=True, verbose_name=_('priority'), db_column='prioridad')
    token= models.CharField(max_length=25, null=True, blank=True, default='', unique=True, verbose_name=_('token'), db_column='token')
    assing= models.BooleanField(default=False, verbose_name=_('assing'), db_column='asignable')
    state= models.BooleanField(default=False, verbose_name=_('state'), db_column='estado')
    color = ColorField(default='#FFFFFF', verbose_name=_('color'), db_column='color')
    type = models.CharField(max_length=100, unique=True, verbose_name=_('type'), db_column='tipo', choices=PERSON_CATEGORY_TYPE)

    class Meta:
        verbose_name = _('Person Category')
        verbose_name_plural = _('Person Categories')
        db_table = f'{APP_LABEL.lower()}_tbn_categoria_persona'
    
    def __str__(self):
        return self.name