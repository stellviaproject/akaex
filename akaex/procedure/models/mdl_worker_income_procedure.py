from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL
from core.models import WorkerIncomeType, WorkerOriginType

from .mdl_worker_procedure import WorkerProcedure


class WorkerIncomeProcedure(BaseAkModel):
    """
        It relates the procedures that are developed for a worker within an organizational
        structure that are of the 'Worker Income' type
    """
    worker_procedure = models.ForeignKey(
                            WorkerProcedure, on_delete=models.CASCADE, 
                            db_column='id_tramite_trabajador', verbose_name=_('worker procedure'),
                            related_name='worker_income_procedures')
    date = models.DateField(verbose_name=_('date'), db_column='fecha')
    worker_income_type = models.ForeignKey(
                            WorkerIncomeType, on_delete=models.CASCADE,
                            db_column='id_tipo_alta_trabajador', verbose_name=_('worker income type'))
    origin = models.ForeignKey(
                            WorkerOriginType, on_delete=models.CASCADE,
                            null=True, db_column='id_origen_trabajador',
                            verbose_name=_('origin'))
    
    class Meta:
        verbose_name = _('Worker Income Procedure')
        verbose_name_plural = _('Worker Income Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_registro_trabajador'

    def __str__(self):
        return f'Trámite de registro a trabajador: {self.worker_procedure.worker_registration.person.full_name}'