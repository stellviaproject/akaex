from core.generics.generic import BaseAkModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL
from structure.models import Speciality
from study_plan.models import AcademicYear, CourseType

class StudyGroup(BaseAkModel):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, default=None, verbose_name=_('speciality'), db_column='especialidad')
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE, default=None, verbose_name=_('course_type'), db_column='tipo_curso')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, default=None, verbose_name=_('academic_year'), db_column='anno_academico')
    short_name = models.CharField(_('short name'), max_length=50, db_column='siglas')


    @property
    def number(self):
        numero=int(self.name[-2:])
        return numero

    class Meta:
        verbose_name = _('Study Group')
        verbose_name_plural = _('Study Groups')
        db_table = f'{APP_LABEL.lower()}_tbd_grupos_studio'
        unique_together = ('name', 'speciality', 'academic_year', 'short_name')

    def __str__(self):
         return f'{str(self.name)}'


