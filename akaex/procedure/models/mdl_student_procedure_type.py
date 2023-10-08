from core.generics.generic import BaseAkModel
from core.models import ProcedureStateType, SchoolSituationType
from django.db import models
from django.utils.translation import gettext as _
from procedure.nom_types import *
from procedure.nom_types import APP_LABEL
from .mdl_teaching_status import TeachingStatus


class StudentProcedureType(BaseAkModel):
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('description'), db_column='descripcion')
    changes_state = models.BooleanField(default=False, verbose_name=_('changes status'), db_column='cambia_estado')
    changes_scholar_situation = models.BooleanField(default=False, verbose_name=_('changes scholar situation'), db_column='cambia_situacion_escolar')
    changes_structure = models.BooleanField(default=False, verbose_name=_('changes structure'), db_column='cambia_estructura')
    initial_states = models.ManyToManyField(TeachingStatus, default=None, blank=True, related_name='initial_states', verbose_name=_('initial status'), db_column='estados_iniciales')
    final_state = models.ForeignKey(TeachingStatus, null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name=_('final status'), db_column='estado_final')
    school_situations = models.ManyToManyField(SchoolSituationType, blank=True, related_name='school_situations', verbose_name=_('school situations'), db_column='situaciones_escolares')
    procedure_type = models.CharField(max_length=100, choices=STUDENT_PROCEDURE_TYPE, default=CONST_PROCEDURE_NONE, verbose_name=_('procedure type'), db_column='tipo_tramite')

    class Meta:
        verbose_name = _('Student Procedure Type')
        verbose_name_plural = _('Student Procedure Types')
        db_table = f'{APP_LABEL.lower()}_tbr_tramite_configuracion'

    def __str__(self):
        return f'Configuración de trámite: {self.procedure_type}'
