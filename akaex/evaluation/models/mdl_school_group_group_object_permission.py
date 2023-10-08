from django.utils.translation import gettext_lazy as _
from django.db import models
from guardian.models import GroupObjectPermissionBase
from core.generics.generic import BaseAkModel
from evaluation.models import SchoolGroup

from evaluation.nom_types import APP_LABEL

class SchoolGroupGroupObjectPermission(BaseAkModel, GroupObjectPermissionBase):
    """Represents the permissions of a group by group docente"""
    name = models.CharField(max_length=2, null=True, default='', editable=False, blank=True, verbose_name=_('name'))
    content_object = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE, verbose_name=_('content_object'), db_column='id_grupo_docente')

    class Meta:
        verbose_name = _('SchoolGroupGroupObjectPermission')
        verbose_name_plural = _('SchoolGroupGroupObjectPermissions')
        db_table = f'{APP_LABEL.lower()}_tbd_permiso_objeto_grupo_grupo_docente'

    def __str__(self):
        return f'{str(self.content_object)} - {str(self.group)}'
