from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL

from .mdl_worker_procedure import WorkerProcedure


class WorkerChangeOfJobPositionProcedure(BaseAkModel):
    """
        It relates the procedures that are developed for a worker within a structure that are of 
        the 'Worker's change of job position' type
    """
    worker_procedure = models.ForeignKey(
                            WorkerProcedure, on_delete=models.CASCADE,
                            db_column='id_tramite_trabajador', verbose_name=_('worker procedure'),
                            related_name='worker_change_of_job_position_procedures')
    
    date = models.DateField(
                            verbose_name=_('change of job position date'), 
                            db_column='fecha_cambio_plaza')
    
    worker_registration = models.ForeignKey('WorkerRegistration', 
                                                on_delete=models.CASCADE, 
                                                verbose_name=_('worker registration'),
                                                db_column='id_registro_trabajador')
    
    class Meta:
        verbose_name = _("Worker's change of job position procedure")
        verbose_name_plural = _("Worker's change of job position procedures")
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_cambio_plaza_trabajador'

    def __str__(self):
        worker_name = self.worker_procedure.worker_registration.person.full_name
        return f'Trámite de cambio de plaza del trabajador: {worker_name}'
    