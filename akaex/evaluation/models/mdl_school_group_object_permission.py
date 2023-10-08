from django.utils.translation import gettext_lazy as _
from django.db import models
from guardian.models import UserObjectPermissionBase
from guardian.models import GroupObjectPermissionBase
from core.generics.generic import BaseAkModel
from evaluation.models import SchoolGroup

from evaluation.nom_types import APP_LABEL

class SchoolGroupUserObjectPermission(BaseAkModel, UserObjectPermissionBase):
    """Represents permissions of a user by group docente"""
    name = models.CharField(max_length=2, null=True, default='', editable=False, blank=True, verbose_name=_('name'), db_column='nombre')
    content_object = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE, verbose_name=_('content_object'), db_column='id_group_docente')

    class Meta:
        verbose_name = _('SchoolGroupUserObjectPermission')
        verbose_name_plural = _('SchoolGroupUserObjectPermissions')
        db_table = f'{APP_LABEL.lower()}_tbd_permiso_objeto_usuario_group_docente'

    def __str__(self):
        return f'{str(self.content_object)} - {str(self.user)}'
