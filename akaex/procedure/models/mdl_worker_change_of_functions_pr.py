from core.generics.generic import BaseAkModel
from core.models import LaboralFunctionType
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import APP_LABEL

from .mdl_worker_procedure import WorkerProcedure


class WorkerChangeOfFunctionsProcedure(BaseAkModel):
    """
        It relates the procedures that are developed to a worker within a structure
        that are of the 'Change of functions' type.
    """
    worker_procedure = models.ForeignKey(
                                WorkerProcedure, on_delete=models.CASCADE,
                                db_column='id_tramite_trabajador', verbose_name=_('worker procedure'),
                                related_name='worker_change_of_functions_procedures')
    change_functions_start_date = models.DateField(
                                verbose_name=_('change of functions start date'), 
                                db_column='fecha_inicio_cambio_funciones')
    change_functions_end_date = models.DateField(
                                verbose_name=_('change of functions end date'), 
                                db_column='fecha_fin_cambio_funciones')
    function = models.ForeignKey(
                                LaboralFunctionType, on_delete=models.CASCADE,
                                db_column='id_funcion_laboral', verbose_name=_('function'))

    
    class Meta:
        verbose_name = _("Worker's change of functions procedure")
        verbose_name_plural = _("Worker's change of functions procedures")
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_cambio_funciones_trabajador'

    def __str__(self):
        worker_name = self.worker_procedure.worker_registration.person.full_name
        return f'Trámite de cambio de funciones del trabajador: {worker_name}'
    