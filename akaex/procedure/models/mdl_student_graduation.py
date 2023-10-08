from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from titulation.models import CertificationGroup

from .mdl_student_procedure import StudentProcedure


class StudentGraduation(BaseAkModel):
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.SET_NULL, null=True, blank=True,
                                          related_name='student_graduation_procedure', verbose_name=_('student procedure'),
                                          db_column='tramite_estudiante')
    certification_group = models.ForeignKey(CertificationGroup, on_delete=models.SET_NULL, null=True, blank=True,
                                            verbose_name=_('certification group'), db_column='grupo_certificacion')

    class Meta:
        verbose_name = _('Student Graduation')
        verbose_name_plural = _('Student Graduations')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_graduacion_estudiante'

    def __str__(self):
        return f'Trámite de graduación a estudiante: {self.student_procedure}'