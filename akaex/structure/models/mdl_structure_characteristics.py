from django.utils.translation import gettext_lazy as _
from django.db import models

from core.generics.generic import BaseAkModel
from structure.models.mdl_structure import Structure
from structure.models.mdl_characteristics import Characteristics

from structure.utils import APP_LABEL

class StructureCharacteristics(BaseAkModel):
    """Represents the relationship between structures and characteristics"""
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'), db_column='id_estructura')
    characteristics = models.ForeignKey(
        Characteristics, on_delete=models.CASCADE, verbose_name=_('characteristics'), db_column='id_caracteristica__categoria_caracteristica')
    existence = models.BooleanField(default=False, verbose_name=_('existence'), db_column='existencia')
    quantity = models.IntegerField(default=0, verbose_name=_('quantity'), db_column='cantidad')

    class Meta:
        verbose_name = _('StructureCharacteristics')
        verbose_name_plural = _('StructureCharacteristics')
        db_table = f'{APP_LABEL.lower()}_tbr_estructura__caracteristica'

    def __str__(self):
        return f'{self.structure.name} -- {self.characteristics.name} -- {self.quantity}'
