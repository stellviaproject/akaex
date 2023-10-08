from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from titulation.nom_types import APP_LABEL
from titulation.models import CertificationGroup
from procedure.models import StudentRegistration

class StudentCertificationGroup(BaseAkModel):
    """Represents students located in each certification group"""
    certification_group = models.ForeignKey(CertificationGroup, on_delete=models.CASCADE, verbose_name=_('certification_group'), db_column='id_grupo_certificacion')
    student_registration = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, verbose_name=_('student_registration'), db_column='id_registro_estudiante')

    class Meta:
        verbose_name = _('Student Certification Group')
        verbose_name_plural = _('Students Certification Groups')
        db_table = f'{APP_LABEL.lower()}_tbr_estudiante__grupo_certificacion'

    def __str__(self):
        return f"{self.student_registration}, {self.certification_group}"