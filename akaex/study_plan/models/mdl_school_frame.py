from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from auditlog.registry import auditlog
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from study_plan.nom_types import APP_LABEL

from .mdl_academic_year import AcademicYear

class SchoolFrame(BaseAkModel):
    """Relates the records that a school frame has (cycles, school periods and academic years)"""
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    school_frame_registry = models.ManyToManyField(AcademicYear, through='SchoolFrameRegistry', through_fields=['school_frame', 'academic_year'], verbose_name=_('school frame registry'), db_column='registro')

    class Meta(BaseAkModel.Meta):
        verbose_name = _('School frame')
        verbose_name_plural = _('School frames')
        db_table = f'{APP_LABEL.lower()}_tbd_marco_lectivo'

    def __str__(self):
        return f'{str(self.name)}'

auditlog.register(SchoolFrame)