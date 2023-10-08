from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL
from core.models import *

class ExternalCenter(BaseAkModel):
    """Represents the external centers"""
    educational_center_type = models.ForeignKey(EducationalCenterType, on_delete=models.SET_NULL, null=True, verbose_name=_('educational_center_type'), db_column='id_centro_educacional')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_("Province"), db_column='id_provincia')
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_("Municipality"), db_column='id_municipio')
    description = models.TextField('Descripción', blank=True, default='', db_column='descripcion')
    forming_organism = models.ForeignKey(OrganismType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('forming_organism'), default=None, db_column='organismo_formador')


    class Meta:
        verbose_name = _('ExternalCenter')
        verbose_name_plural = _('ExternalCenters')
        db_table = f'{APP_LABEL.lower()}_tbd_centro_externo'

    def __str__(self):
        return self.name