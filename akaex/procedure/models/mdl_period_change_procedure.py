from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from planning.models import Course
from study_plan.models import AcademicYear, SchoolPeriod
from .mdl_student_procedure import StudentProcedure


class PeriodChangeProcedure(BaseAkModel):
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.CASCADE, default=None, verbose_name=_('student procedure'), db_column='tramite_estudiante')
    origen_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='%(class)s_origen_year', default=None, verbose_name=_('origen_year'), db_column='id_anno_procedencia')
    destination_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='%(class)s_destination_year', default=None, verbose_name=_('destination_year'), db_column='id_anno_detino')
    origen_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, related_name='%(class)s_origen_period', default=None, verbose_name=_('origen_period'), db_column='id_periodo_procedencia')
    destination_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, related_name='%(class)s_destination_period', verbose_name=_('destination_period'), default=None, db_column='id_periodo_destino')
    destination_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, verbose_name=_('destination_course'), db_column='id_curso_detino')

    class Meta:
        verbose_name = _('School Period Change')
        verbose_name_plural = _('School Period Changes')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_cambio_periodo_lectivo_estudiante'

    def __str__(self):
        return f'Trámite cambio de periodo lectivo a estudiante: {self.student_procedure}'
