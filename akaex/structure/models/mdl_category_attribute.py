from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *

class CategoryAttribute(BaseAkModel):
    """Represents the attributes of a category"""
    class Meta:
        verbose_name = _('CategoryAttribute')
        verbose_name_plural = _('CategoryAttributes')
        db_table = f'{APP_LABEL.lower()}_tbn_atributo_categoria'

    def __str__(self):
        return self.name