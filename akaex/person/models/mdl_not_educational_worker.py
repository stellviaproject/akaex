from core.generics.generic import BaseAkModel
from core.models import *
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.signals import post_delete, post_save
from django.utils.translation import gettext as _
from person.utils import APP_LABEL
from structure.models import *

from .mdl_person import Person
from .mdl_person_structure import (associate_person_structure,
                                   delete_person_structure)


class NotEducationalWorker(BaseAkModel):
    """ It relates all the data about a person who is a not educational worker"""
    name = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name=_('name'))
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'), db_column='estructura')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')

    # This field is not in the document
    profession = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('profession'), db_column='profesion')

    def __str__(self):
        return f'{self.person} -- Structure: {self.structure_id}'

    class Meta:
        verbose_name = _('Not Educational Worker')
        verbose_name_plural = _('Not Educational Workers')
        indexes = [
            models.Index(fields=['structure']),
        ]
        constraints = [
            UniqueConstraint(fields=['structure', 'person'], name='uniq_not_educ_worker')
        ]
        db_table = f'{APP_LABEL.lower()}_tbd_trabajador_no_docente'


# post_save.connect(associate_person_structure, sender=NotEducationalWorker)
# post_delete.connect(delete_person_structure, sender=NotEducationalWorker)
