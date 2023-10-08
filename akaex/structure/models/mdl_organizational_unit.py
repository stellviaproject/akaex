from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *
# from .mdl_structure_type import StructureType
from .mdl_structure_eductive_center_type import EducativeCenter
from .mdl_speciality_modality import Speciality

class OrganizatinalUnit(BaseAkModel):
    """OrganizatinalUnit CRUD"""
    center_type = models.ForeignKey(EducationalCenterType, on_delete=models.SET_NULL, null=True, default='', verbose_name=_('center_type'), db_column='id_tipo_centro')
    educatinal_center = models.ForeignKey(EducativeCenter, on_delete=models.SET_NULL, related_name='edcenters', related_query_name="edcenter", null=True, verbose_name=_('educatinal_center'), db_column='id_centro_educativo')
    description = models.CharField(max_length=300, default='', verbose_name=_('description'), db_column='descripcion')
    specialities = models.ManyToManyField(Speciality, through='evaluation.OrganizativeUnitSpeciality', through_fields=['organizative_unit', 'speciality'],  default=None, blank=True, verbose_name=_('speciality'))

    class Meta:
        verbose_name = _('OrganizatinalUnit')
        verbose_name_plural = _('OrganizatinalUnits')
        db_table = f'{APP_LABEL.lower()}_tbd_unidad_organizativa'
        unique_together = ('name', 'educatinal_center')

    def __str__(self):
        return self.name