from django.utils.translation import gettext_lazy as _
from django.db import models
from guardian.models import UserObjectPermissionBase
from guardian.models import GroupObjectPermissionBase
from core.generics.generic import BaseAkModel
from structure.models.mdl_structure import Structure

from structure.utils import APP_LABEL

class StructureUserObjectPermission(BaseAkModel, UserObjectPermissionBase):
    """Represents permissions of a user by structure"""
    name = models.CharField(max_length=2, null=True, default='', editable=False, blank=True, verbose_name=_('name'), db_column='nombre')
    content_object = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('content_object'), db_column='id_structura')

    class Meta:
        verbose_name = _('StructureUserObjectPermission')
        verbose_name_plural = _('StructureUserObjectPermissions')
        db_table = f'{APP_LABEL.lower()}_tbd_permiso_objeto_usuario_estructura'

    def __str__(self):
        return f'{str(self.content_object)} - {str(self.user)}'
