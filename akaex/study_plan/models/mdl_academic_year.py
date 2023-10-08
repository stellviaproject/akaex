from django.utils.translation import gettext as _
from django.db import models
from django.conf import settings
from core.generics.generic import BaseAkModel
from auditlog.registry import auditlog
from study_plan.nom_types import APP_LABEL


class AcademicYear(BaseAkModel):
    """Relates the academic years that will be part of the school frames"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    code = models.CharField(max_length=2, default=None, null=True, blank=True, verbose_name=_('code'), db_column='codigo')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('Academic year')
        verbose_name_plural = _('Academic years')
        db_table = f'{APP_LABEL.lower()}_tbd_año_academico'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(AcademicYear)