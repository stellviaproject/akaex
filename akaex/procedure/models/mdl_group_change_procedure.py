from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from datetime import date
from planning.models import Course
from procedure.nom_types import APP_LABEL
from evaluation.models import StudyGroup
from .mdl_student_procedure import StudentProcedure
from .mdl_student_registration import StudentRegistration


class GroupChangeProcedure(BaseAkModel):
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.CASCADE, verbose_name=_('student registration'), db_column='registro_estudiante', default=None)
    origen_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='%(class)s_origen_course',null=True, blank=True, default=None, verbose_name=_('origen_course'), db_column='id_curso_procedencia')
    origen_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='%(class)s_origen_group',null=True, blank=True, default=None, verbose_name=_('origen_group'), db_column='id_grupo_procedencia')
    destination_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='%(class)s_destination_course', default=None, verbose_name=_('destination_course'), db_column='id_curso_destino')
    destination_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='%(class)s_destination_group', verbose_name=_('destination_group'), default=None, db_column='id_grupo_destino')


    class Meta:
        verbose_name = _('Group Change')
        verbose_name_plural = _('Group Changes')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_cambio_grupo_estudiante'

    def __str__(self):
        return f'Trámite cambio de grupo a estudiante: {self.student_procedure}'
