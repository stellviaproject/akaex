from django.utils.translation import gettext as _
from django.db import models
from core.generics.generic import BaseAkModel
from structure.utils import APP_LABEL

class Speciality(BaseAkModel):
    """Represents the specialities"""
    short_name = models.CharField(_('short name'), unique=True, max_length=50, db_column='siglas')
    description = models.CharField(_('description'), max_length=255, db_column='descripcion')
    is_mined_type = models.BooleanField(default=False, verbose_name=_('is_mined_type'), db_column='tipo_mined')


    class Meta:
        verbose_name = _('Speciality')
        verbose_name_plural = _('Specialties')
        db_table = f'{APP_LABEL.lower()}_tbd_especialidad'

    def __str__(self):
        return self.name