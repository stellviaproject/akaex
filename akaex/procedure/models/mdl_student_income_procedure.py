from datetime import datetime
from django.conf import settings
from core.generics.generic import BaseAkModel
from django.utils.translation import gettext as _
from django.db import models
from procedure.nom_types import APP_LABEL

from .mdl_student_procedure import StudentProcedure
from core.generics.generic import BaseAkModel


def procedure_doc_storage_path(instance, filename):
    """
    Files will be uploaded to:
    MEDIA_ROOT/<procedure-docs>/<register>/<current_date>/<filename>
    """

    now = datetime.now()  # current date
    current_date = now.strftime("%Y/%m/%d")

    path = f'procedure-docs/register/{current_date}/{filename}'

    return path


class StudentIncomeProcedure(BaseAkModel):
    
    student_procedure = models.ForeignKey(StudentProcedure, on_delete=models.CASCADE, verbose_name=_('student procedure'), db_column='tramite_estudiante')
    date = models.DateField(auto_now=True, verbose_name=_('date'), db_column='fecha')
    doc = models.FileField(upload_to=procedure_doc_storage_path, default=None, null=True, blank=True, verbose_name=_('doc'), db_column='doc')


    class Meta:
        verbose_name = _('Student Income Procedure')
        verbose_name_plural = _('Student Income Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_registro_estudiante'

    def __str__(self):
        return f'Trámite de registro a estudiante: {self.student_procedure}'
