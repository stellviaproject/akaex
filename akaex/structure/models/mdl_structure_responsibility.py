from django.utils.translation import gettext_lazy as _
from django.db import models

from core.generics.generic import BaseAkModel
from structure.models.mdl_structure import Structure
from structure.models.mdl_responsibility import Responsibility

from structure.utils import APP_LABEL

class StructureResponsibility(BaseAkModel):
    """Represents the relationship between structures and responsibilities"""
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'), db_column='id_estructura')
    responsibility = models.ForeignKey(
        Responsibility, on_delete=models.CASCADE, verbose_name=_('responsibility'), db_column='id_responsabilidad')
    amount = models.PositiveIntegerField(default=0, verbose_name=_('amount'), db_column='cantidad')
    ocupada = models.PositiveIntegerField(default=0, verbose_name=_('ocupada'), db_column='ocupada')

    class Meta:
        verbose_name = _('StructureResponsibility')
        verbose_name_plural = _('StructureResponsibilities')
        db_table = f'{APP_LABEL.lower()}_tbr_estructura__responsabilidad'

    def __str__(self):
        return f'{self.structure.name} -- {self.responsibility.name}'
