from core.generics.generic import BaseAkModel
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import *
from structure.models import Responsibility, Structure

from .mdl_worker_registration import WorkerRegistration


class WorkerProcedure(BaseAkModel):
    """
        It relates the procedures that are carried out to a worker within the organizational
        structure where he or she is employed.
    """
    worker_registration = models.ForeignKey(
                        WorkerRegistration, on_delete=models.CASCADE, 
                        db_column='id_registro_trabajador', verbose_name=_('worker'))
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, verbose_name=_('structure'))
    responsibility = models.ForeignKey(
                Responsibility, on_delete=models.CASCADE, db_column='id_responsabilidad',
                verbose_name=_('responsibility'))
    start_date = models.DateField(
                        auto_now=True, verbose_name=_('start date'), 
                        db_column='fecha_inicio')
    end_date = models.DateField(
                        verbose_name=_('end date'), 
                        null=True, blank=True, db_column='fecha_fin')
    state = models.CharField(
                        max_length=50, choices=PROCEDURE_STATES, 
                        default=CONST_PROCEDURE_STATE_INITIATED, verbose_name=_('status'),
                        db_column='estado')
    previous_procedure = models.ForeignKey(
                        'WorkerProcedure', on_delete=models.SET_NULL, 
                        null=True, blank=True, verbose_name=_('previous procedure'), 
                        db_column='tramite_anterior')
    processor_person_id = models.UUIDField(
                        null=True, default=None, blank=True, 
                        verbose_name=_('processor person id'), 
                        db_column='persona_procesa')
    procedure_type = models.CharField(
                        max_length=100, choices=WORKER_PROCEDURE_TYPE, 
                        default=CONST_PROCEDURE_NONE, verbose_name=_('procedure type'), 
                        db_column='tipo_tramite')
    
    class Meta:
        verbose_name = _('Worker Procedure')
        verbose_name_plural = _('Worker Procedures')
        db_table = f'{APP_LABEL.lower()}_tbd_tramite_trabajador'

    def __str__(self):
        return f'Trámite general del trabajador - {self.name}'
