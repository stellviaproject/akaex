from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import *
from core.models import WorkerUnsubscribementType, WorkerUnsubscribementReasonType

from .mdl_worker_procedure import WorkerProcedure


class WorkerUnsubscribementProcedure(BaseAkModel):
    """
        It relates the procedures that a worker develops within a structure that are of the 
        type 'Worker Unsubscribement'
    """
    worker_procedure = models.ForeignKey(
                            WorkerProcedure, on_delete=models.CASCADE,
                            db_column='id_tramite_trabajador', verbose_name=_('worker procedure'),
                            related_name='worker_unsubscribement_procedures')
    date = models.DateField(
                            verbose_name=_('date'), 
                            db_column='fecha_baja_trabajador')
    worker_unsubscribement_type = models.ForeignKey(
                            WorkerUnsubscribementType, on_delete=models.CASCADE,
                            db_column='id_tipo_baja', verbose_name=_('worker unsubscribement type'))
    worker_unsubscribement_reason = models.ForeignKey(
                            WorkerUnsubscribementReasonType, on_delete=models.CASCADE,
                            db_column='id_motivo_baja_trabajador', null=True,
                            verbose_name=_('worker unsubscribement reason'))
    
    class Meta:
        verbose_name = _('Worker Unsubscribement Procedure')
        verbose_name_plural = _('Worker Unsubscribement Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_baja_trabajador'

    def __str__(self):
        worker_name = self.worker_procedure.worker_registration.person.full_name
        return f'Trámite de baja del trabajador: {worker_name}'
