from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *
from .mdl_organizational_unit import OrganizatinalUnit
from .mdl_structure import Structure
from .mdl_structure_eductive_center_type import EducativeCenter
from evaluation.models.mdl_study_group import StudyGroup

class CenterGroup(BaseAkModel):
    """OrganizatinalUnit CRUD"""
    group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='center_group', verbose_name=_('group'), db_column='id_group')
    educatinal_center = models.ForeignKey(EducativeCenter, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='center_group', verbose_name=_('educatinal_center'), db_column='id_centro_educativo')
    organizatinal_unit = models.ForeignKey(OrganizatinalUnit, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='center_group', verbose_name=_('organizatinal_unit'), db_column='id_unidad_organizacional')

    class Meta:
        verbose_name = _('CenterGroup')
        verbose_name_plural = _('CenterGroups')
        db_table = f'{APP_LABEL.lower()}_tbd_grupo_centro'


    def __str__(self):
        return f'{str(self.group)} - {str(self.educatinal_center)} - {str(self.organizatinal_unit)} '
