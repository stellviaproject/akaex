from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from evaluation.nom_types import APP_LABEL

from planning.models import Course
from structure.models import Structure, OrganizatinalUnit


class Cloister(BaseAkModel):
    """
    List the cloisters registered for each educational center or organizational unit
    by school year.
    """
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                               verbose_name=_('course'), db_column='curso')
    center = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                               verbose_name=_('center'), db_column='centro')
    unity = models.ForeignKey(OrganizatinalUnit, on_delete=models.SET_NULL, null=True, blank=True, default=None,
                              verbose_name=_('unity'), db_column='unidad')

    class Meta:
        verbose_name = _('Cloister')
        verbose_name_plural = _('Cloisters')
        db_table = f'{APP_LABEL.lower()}_tbd_cloister'
        unique_together = ('course', 'center', 'unity')

    def __str__(self):
        return f'{str(self.course)} - {str(self.center)} - {str(self.unity)}'