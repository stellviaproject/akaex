from django.utils.translation import gettext_lazy as _
from django.db import models

from core.generics.generic import BaseAkModel
from structure.models.mdl_structure import Structure
from structure.models.mdl_building import Building

from structure.utils import APP_LABEL

class StructureBuilding(BaseAkModel):
    """Represents the relationship between structures and buildings"""
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'), db_column='id_estructura')
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, verbose_name=_('inmueble'), db_column='inmueble')

    class Meta:
        verbose_name = _('StructureBuilding')
        verbose_name_plural = _('StructureBuildings')
        db_table = f'{APP_LABEL.lower()}_tbr_estructura__inmueble'

    def __str__(self):
        return f'{self.structure.name} -- {self.building.name}'
