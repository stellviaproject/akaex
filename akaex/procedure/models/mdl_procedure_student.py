from core.generics.generic import BaseAkModel
from core.models import DiscapacityType, DiseaseType, OrphanType
from django.db import models
from django.utils.translation import gettext as _
from person.models import Person
from procedure.nom_types import APP_LABEL

from .mdl_legal_tutor import LegalTutor


class ProcedureStudent(BaseAkModel):
    """
        Used for storage student's common data
    """
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('name'))
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('person'), db_column='persona')
    legal_tutors = models.ManyToManyField(LegalTutor, blank=True, related_name='legal_tutors', verbose_name=_('legal tutors'), db_column='tutores_legales')
    discapacity = models.ForeignKey(DiscapacityType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('discapacity'), db_column='discapacidad')
    orphan = models.ForeignKey(OrphanType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('orphan'), db_column='huerfano')

    diseases = models.ManyToManyField(DiseaseType, blank=True, related_name='diseases', verbose_name=_('disease'))

    class Meta:
        verbose_name = _('Procedure Student')
        verbose_name_plural = _('Procedure Students')
        db_table = f'{APP_LABEL.lower()}_tbr_estudiante_tramite'

    def __str__(self):
        return f'{str(self.name)}'