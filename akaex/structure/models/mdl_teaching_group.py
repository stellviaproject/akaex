from django.utils.translation import gettext_lazy as _
from django.db import models

from core.generics.generic import BaseAkModel
from structure.models.mdl_structure import Structure

from structure.utils import APP_LABEL

class TeachingGroup(BaseAkModel):
    """Represents the teaching groups"""
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, related_name='groups', verbose_name=_('structure'), db_column='id_estructura')

    class Meta:
        verbose_name = _('TeachingGroup')
        verbose_name_plural = _('TeachingGroups')
        db_table = f'{APP_LABEL.lower()}_tbd_grupo_ensennanza'
