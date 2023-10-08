from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint
from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from .mdl_student import Student
from structure.models import *
from person.utils import APP_LABEL

class StudentGroup(BaseAkModel):
    """ It relates the student with a teaching group and a structure"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('student'), db_column='estudiante')
    group = models.ForeignKey(TeachingGroup, on_delete=models.CASCADE, verbose_name=_('group'), db_column='grupo')
    structure = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, editable=False, verbose_name=_('structure'), db_column='estructura')

    def clean(self):
        if self.student.structure_id != self.group.structure_id:
            raise ValidationError(_("Group structure and Student structure doesnt mach"))

    def __str__(self):
        return f'{str(self.group)} - Structure: {self.student.structure_id}'

    def save(self, *args, **kwargs):
        self.structure_id = self.student.structure_id
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Student Group')
        verbose_name_plural = _('Student Groups')
        indexes = [
            models.Index(fields=['student', 'group']),
        ]
        constraints = [
            UniqueConstraint(fields=['student', 'group'], name='uniq_student_group'),
            # UniqueConstraint(fields=['user'], condition=Q(status='DRAFT'), name='unique_draft_user')
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_grupo_estudiante'