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
from .mdl_tutor import Tutor


class Student(BaseAkModel):
    """ It represent a person who is a student"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    no_expedient = models.CharField(max_length=50, verbose_name=_('no. expedient'), db_column='no_expediente')
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'), db_column='estructura')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    status = models.ForeignKey(StudentStatusType, on_delete=models.SET_NULL, null=True, verbose_name=_('status'), db_column='estado')
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True, db_column='tutor')
    productive_activity = models.ForeignKey(ProductiveActivityType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('productive activity'), db_column='actividad_productiva')

    # This field is not in the document, but the student can have an academic level
    # scholar_level = models.CharField(max_length=100, null=True, blank=True)

    groups = models.ManyToManyField(TeachingGroup, through='StudentGroup', related_name='students',
                                    through_fields=('student', 'group'), verbose_name=_('groups'), db_column='grupos')

    tutors = models.ManyToManyField(Tutor, through='StudentTutor', related_name='students',
                                    through_fields=('student', 'tutor'), verbose_name=_('tutors'), db_column='tutores')

    def __str__(self):
        return f'{self.person} -- Structure: {self.structure_id}'

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        indexes = [
            models.Index(fields=['structure']),
        ]
        constraints = [
            UniqueConstraint(fields=['structure', 'person'], name='uniq_student')
        ]
        db_table = f'{APP_LABEL.lower()}_tbr_estudiante'


# post_save.connect(associate_person_structure, sender=Student)
# post_delete.connect(delete_person_structure, sender=Student)
