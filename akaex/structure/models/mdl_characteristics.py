from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *
from .mdl_structure_type import StructureType

class Characteristics(BaseAkModel):
    """Represents the characteristics"""
    characteristic_type = models.ForeignKey(CharacteristicType, on_delete=models.SET_NULL, null=True, verbose_name=_('characteristic_type'), db_column='id_caracteristica')
    characteristic_category_type = models.ForeignKey(CharacteristicCategoryType, on_delete=models.SET_NULL, null=True, verbose_name=_('characteristic_category_type'), db_column='id_categoria_caracteristica')
    structure_type = models.ForeignKey(StructureType, on_delete=models.SET_NULL, null=True, verbose_name=_('structure_type'), db_column='tipo_estructura')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')

    class Meta:
        verbose_name = _('Characteristics')
        verbose_name_plural = _('Characteristics')
        db_table = f'{APP_LABEL.lower()}_tbr_caracteristica__categoria_caracteristica'


    def __str__(self):
        return self.name