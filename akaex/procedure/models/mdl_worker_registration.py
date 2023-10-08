from core.generics.generic import BaseAkModel
from core.models import ContractType, PersonCategoryType, WorkerStateType
from django.db import models
from django.utils.translation import gettext as _
from person.models import Person
from procedure.nom_types import (APP_LABEL, CONST_PROCEDURE_NONE,
                                 WORKER_PROCEDURE_TYPE)
from structure.models import Responsibility, Structure


class WorkerRegistration(BaseAkModel):
    """
        Represents the record that is made to a worker within a structure
        performing a responsibility
    """
    person = models.ForeignKey(
                Person, on_delete=models.CASCADE, db_column='id_persona',
                verbose_name=_('person'))
    structure = models.ForeignKey(
                Structure, on_delete=models.CASCADE, db_column='id_estructura',
                verbose_name=_('structure'))
    responsibility = models.ForeignKey(
                Responsibility, on_delete=models.CASCADE, db_column='id_responsabilidad',
                verbose_name=_('responsibility'))
    category = models.ForeignKey(
                PersonCategoryType, on_delete=models.CASCADE, db_column='id_categoria_persona',
                verbose_name=_('category'))
    contract = models.ForeignKey(
                ContractType, on_delete=models.CASCADE, db_column='id_tipo_contrato',
                verbose_name=_('contract'))
    qualified = models.BooleanField(
                null=True, blank=True, db_column='titulado', verbose_name=_('qualified'))
    does_study = models.BooleanField(
                null=True, blank=True, db_column='estudia', verbose_name=_('does study'))
    professional = models.BooleanField(
                null=True, blank=True, db_column='es_profesional', verbose_name=_('professional'))
    member_of_directors_board = models.BooleanField(
                null=True, blank=True,
                db_column='miembro_consejo_direccion',
                verbose_name=_('member of directors board'))
    state = models.ForeignKey(
                WorkerStateType, on_delete=models.CASCADE, db_column='id_estado_trabajador',
                verbose_name=_('state'))
    occupied_position = models.BooleanField(
                default=True, db_column='alta', verbose_name=_('occupied position'))
    previous_procedure = models.ForeignKey(
                'WorkerProcedure', on_delete=models.SET_NULL, null=True, blank=True, 
                verbose_name=_('previous procedure'), db_column='tramite_anterior')
    procedure_type = models.CharField(
                max_length=100, choices=WORKER_PROCEDURE_TYPE, 
                default=CONST_PROCEDURE_NONE, verbose_name=_('procedure type'), 
                db_column='tipo_tramite')
    
    class Meta:
        verbose_name = _('Worker Registration')
        verbose_name_plural = _('Worker Registrations')
        db_table = f'{APP_LABEL.lower()}_tbd_registro_trabajador'
    
    def __str__(self):
        return f'{self.person.full_name}, {self.responsibility} en {self.structure}'
