from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL
from evaluation.models import Cloister

from person.models import Person
from study_plan.models import Subject


class Professor(BaseAkModel):
    """
    It lists the professors who belong to a faculty in a course within an educational center
    or organizational unit, in addition to the subject (s) taught.
    """
    worker = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                               verbose_name=_('worker'), db_column='trabajador')
    subjects = models.ManyToManyField(Subject, blank=True, default=None,
                                      verbose_name=_('subjects'), db_column='asignaturas')
    cloister = models.ForeignKey(
        Cloister,
        on_delete=models.SET_NULL, null=True, blank=True, default=None,
        db_column='claustro',
        verbose_name=_('cloister')
    )

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professors')
        db_table = f'{APP_LABEL.lower()}_tbd_professor'
#        unique_together = ('worker', 'cloister')

    def __str__(self):
        return f'{self.worker} {self.cloister}'

