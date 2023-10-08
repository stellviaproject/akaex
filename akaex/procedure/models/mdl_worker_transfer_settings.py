from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import *

from .mdl_worker_procedure import WorkerProcedure


class WorkerTransferSettings(BaseAkModel):
    """
        It relates the procedures that are developed for a worker who was discharged from a
        structure due to transfer and is not going to join another
    """
    worker_procedure = models.ForeignKey(
                            WorkerProcedure, on_delete=models.CASCADE,
                            db_column='id_tramite_trabajador', verbose_name=_('worker procedure'),
                            related_name='worker_transfer_settings')
    worker_unsubscribement_date = models.DateField(
                            verbose_name=_('worker unsubscribement date'), 
                            db_column='fecha_baja_trabajador')
    
    class Meta:
        verbose_name = _('Worker Transfer Setting')
        verbose_name_plural = _('Worker Transfer Settings')
        db_table = f'{APP_LABEL.lower()}_tbd_ajustes_traslados_trabajador'

    def __str__(self):
        worker_name = self.worker_procedure.worker_registration.person.full_name
        return f'Ajustes de traslados - {worker_name} - {self.job_discharge_date}'
