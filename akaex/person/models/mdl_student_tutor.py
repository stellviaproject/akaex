from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from .mdl_tutor import Tutor
from .mdl_student import Student
from structure.models import *
from person.utils import APP_LABEL

class StudentTutor(BaseAkModel):
    """ It relates the student with a tutor and a structure"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('student'), db_column='estudiante')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name=_('tutor'), db_column='tutor')
    structure = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, editable=False, verbose_name=_('structure'), db_column='estructura')

    def __str__(self):
        return f'{str(self.tutor)} - Structure: {self.student.structure_id}'

    def save(self, *args, **kwargs):
        self.structure_id = self.student.structure_id
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Student Tutor')
        verbose_name_plural = _('Student Tutors')
        indexes = [
            models.Index(fields=['student', 'tutor']),
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_estudiante_tutor'