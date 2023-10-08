from datetime import date, datetime
from core.generics.generic import BaseAkModel
from core.models import SessionType
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from structure.models import Structure, ExternalCenter
from study_plan.models import CourseType, StudyModality

from .mdl_procedure_reason import ProcedureReason
from .mdl_student_procedure import StudentProcedure
from .mdl_way_entry import WayEntry

def procedure_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<procedure-docs>/<enrollment>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'procedure-docs/enrollment/{current_date}/{filename}'

    return path

class StudentEnrollmentProcedure(BaseAkModel):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('name'))
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name=_('student procedure'), db_column='tramite_estudiante')
    origin_center = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name=_('origin center'), db_column='centro_origen')
    way_of_entry = models.ForeignKey(WayEntry, on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name=_('way of entry'), db_column='via_ingreso')
    #procedure_reason = models.ForeignKey(ProcedureReason, on_delete=models.SET_NULL, null=True, blank=True,
    #                                     verbose_name=_('procedure reason'), db_column='motivo_tramite')
    #external_center = models.ForeignKey(ExternalCenter, on_delete=models.SET_NULL, null=True, blank=True,
    #                                    verbose_name=_('external_center'), db_column='centro_externo')
    enrollment_date = models.DateField(auto_now=True, null=True, blank=True, db_column='fecha_matricula', verbose_name=_('enrollment date'))

    doc = models.FileField(upload_to=procedure_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('doc'), db_column='doc')

    class Meta:
        verbose_name = _('Student Enrollment Procedure')
        verbose_name_plural = _('Student Enrollment Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_matricula_estudiante'

    def __str__(self):
        return f'Trámite de matrícula a estudiante: {self.student_procedure}'
