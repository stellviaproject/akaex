from core.generics.generic import BaseAkModel
from core.models import *
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.signals import post_delete, post_save
from django.utils.translation import gettext as _
from person.utils import APP_LABEL
from structure.models import *

from .mdl_person import Person
from .mdl_person_structure import (associate_person_structure,
                                   delete_person_structure)


class EducationalWorker(BaseAkModel):
    """ It relates all the data about a person who is an educational worker"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'), db_column='estructura')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    # person_type = models.OneToOneField(PersonType, on_delete=models.CASCADE, related_name='educational_worker')
    teaching_category = models.ForeignKey(TeachingCategoryType, on_delete=models.SET_NULL, null=True, verbose_name=_('teaching category'), db_column='categoria_enseñanza')
    specialty = models.ForeignKey(TeacherSpecialityType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('specialty'), db_column='especialidad')
    teaching_status = models.ForeignKey(TeacherStatusType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('teaching status'), db_column='estado_enseñanza')

    # these three fields are not in the document
    scientific_grade = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('scientific grade'), db_column='grado_cientifico')
    research_category = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('research category'), db_column='categoria_investigativa')
    profession = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('profession'), db_column='profesion')

    groups = models.ManyToManyField(TeachingGroup, through='EducationalWorkerGroup', related_name='teachers',
                                    through_fields=('teacher', 'group'), verbose_name=_('groups'), db_column='grupos')

    def __str__(self):
        return f'{self.person} -- Structure: {self.structure_id}'

    class Meta:
        verbose_name = _('Educational Worker')
        verbose_name_plural = _('Educational Workers')
        indexes = [
            models.Index(fields=['structure']),
        ]
        constraints = [
            UniqueConstraint(fields=['structure', 'person'], name='uniq_educ_worker')
        ]
        db_table = f'{APP_LABEL.lower()}_tbr_trabajador_docente'


# post_save.connect(associate_person_structure, sender=EducationalWorker)
# post_delete.connect(delete_person_structure, sender=EducationalWorker)
