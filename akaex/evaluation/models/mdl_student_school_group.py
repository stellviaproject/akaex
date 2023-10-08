from core.generics.generic import BaseAkModel
from django.db import models
from procedure.models import StudentRegistration
from django.utils.translation import gettext as _
from evaluation.nom_types import (APP_LABEL, PLACEMENT_CONCEPTS, 
    PLACEMENT_CONCEPTS_DEFAULT)

from .mdl_school_group import SchoolGroup


class StudentSchoolGroup(BaseAkModel):

    school_group = models.ForeignKey(
        SchoolGroup,
        on_delete=models.CASCADE,
        verbose_name=_('School Group'),
        db_column='id_grupo_docente'
    )

    student_registration = models.ForeignKey(
        StudentRegistration,
        on_delete=models.CASCADE,
        verbose_name=_('Student Registration'),
        db_column='id_registro_estudiante'
    )
    
    placement_concept = models.CharField(
        default=PLACEMENT_CONCEPTS_DEFAULT,
        choices=PLACEMENT_CONCEPTS,
        verbose_name=_('Concepto de ubicacion'),
        db_column='concepto_ubicacion',
        max_length=100
    )
    
    class Meta:
        verbose_name = _('Student School Group')
        verbose_name_plural = _('Students School Groups')
        db_table = f'{APP_LABEL.lower()}_tbr_estudiante__grupo_docente'

    def __str__(self):
        student_name = self.student_registration.student.person.full_name
        return f'{student_name}, {self.school_group}'