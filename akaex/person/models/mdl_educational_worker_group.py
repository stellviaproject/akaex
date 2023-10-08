from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from .mdl_educational_worker import EducationalWorker
from structure.models import *
from person.utils import APP_LABEL

class EducationalWorkerGroup(BaseAkModel):
    """ It relates an educational worker with a structure and a teaching group"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    teacher = models.ForeignKey(EducationalWorker, on_delete=models.CASCADE, verbose_name=_('teacher'), db_column='profesor')# Represents an educational worker
    group = models.ForeignKey(TeachingGroup, on_delete=models.CASCADE, verbose_name=_('group'), db_column='grupo')
    structure = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, editable=False, verbose_name=_('structure'), db_column='estructura')

    def clean(self):
        if self.teacher.structure_id != self.group.structure_id:
            raise ValidationError(_("Group structure and Teacher structure doesnt mach"))

    def __str__(self):
        return f'{str(self.group)} - Structure: {self.teacher.structure_id}'

    def save(self, *args, **kwargs):
        self.structure_id = self.teacher.structure_id
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Educational Worker Group')
        verbose_name_plural = _('Educational Worker Groups')
        indexes = [
            models.Index(fields=['teacher', 'group']),
        ]
        constraints = [
            UniqueConstraint(fields=['teacher', 'group'], name='uniq_teacher_group')
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_grupo_trabajador_docente'