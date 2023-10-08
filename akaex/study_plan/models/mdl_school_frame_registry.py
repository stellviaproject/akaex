from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from core.generics.generic import BaseAkModel
from core.models import Nomenclator, NOM_TYPE, BaseType
from auditlog.registry import auditlog
from study_plan.nom_types import APP_LABEL

from .mdl_school_frame import SchoolFrame
from .mdl_academic_year import AcademicYear
from .mdl_school_period import SchoolPeriod
from .mdl_cycle import Cycle


class SchoolFrameRegistry(BaseAkModel):
    """Relates the records of the school frame (academic year, school period and cycle) related to it"""
    name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('name'), db_column='nombre')
    school_frame = models.ForeignKey(SchoolFrame, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('school frame'), default=None, db_column='marco_lectivo')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name=_('academic year'), db_column='año')
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name=_('school period'), db_column='periodo')
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name=_('cycle'), db_column='ciclo')
    order = models.IntegerField(null=False, verbose_name=_('order'))

    class Meta(BaseAkModel.Meta):
        verbose_name = _('School frame registry')
        verbose_name_plural = _('School frame registries')
        db_table = f'{APP_LABEL.lower()}_tbr_registro_marco_lectivo'

    def __str__(self):
        return f'{str(self.academic_year)} - {str(self.school_period)}'

auditlog.register(SchoolFrameRegistry)