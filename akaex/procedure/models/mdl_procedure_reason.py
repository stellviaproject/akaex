from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL

from .mdl_student_procedure_type import StudentProcedureType


class ProcedureReason(BaseAkModel):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    procedures = models.ManyToManyField(StudentProcedureType, default=None,  blank=True, verbose_name=_('procedures'),
                                        db_column='tramites')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    status = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('status'),
                              db_column='estado')

    class Meta:
        verbose_name = _('Procedure Reason')
        verbose_name_plural = _('Procedure Reasons')
        db_table = f'{APP_LABEL.lower()}_tbd_motivo_tramite'

    def __str__(self):
        return f'{self.name}'
