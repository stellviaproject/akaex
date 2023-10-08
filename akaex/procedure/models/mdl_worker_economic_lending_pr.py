from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from core.models import EconomicLendingReasonType

from .mdl_worker_procedure import WorkerProcedure


class WorkerEconomicLendingProcedure(BaseAkModel):
    """
        It relates the procedures that are developed to a worker within a structure
        that are of the 'Worker economic lending' type
    """
    worker_procedure = models.ForeignKey(
                                WorkerProcedure, on_delete=models.CASCADE,
                                db_column='id_tramite_trabajador', verbose_name=_('worker'),
                                related_name='worker_economic_lending_procedures')
    economic_lending_start_date = models.DateField(
                                verbose_name=_('economic lending start date'), 
                                db_column='fecha_inicio_prestacion_economica')
    economic_lending_end_date = models.DateField(
                                verbose_name=_('economic lending end date'), 
                                db_column='fecha_fin_prestacion_economica')
    inactivity_period = models.IntegerField(
                                null=True, db_column='periodo_inactividad',
                                verbose_name=_('inactivity period'))
    reason = models.ForeignKey(
                                EconomicLendingReasonType, on_delete=models.CASCADE,
                                db_column='id_motivo_prestacion_economica',
                                verbose_name='reason')
    
    class Meta:
        verbose_name = _('Worker Economic Lending Procedure')
        verbose_name_plural = _('Worker Economic Lending Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_prestacion_economica_a_trabajador'

    def __str__(self):
        worker_name = self.worker_procedure.worker_registration.person.full_name
        return f'Trámite de prestación económica a trabajador: {worker_name}'
    