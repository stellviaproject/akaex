from django.utils.translation import gettext as _
from django.db import models
from core.models import *
from core.generics.generic import BaseAkModel
from person.utils import APP_LABEL

class ProcedureConfiguration(BaseAkModel):
    """ It represents a procedure configuration"""
    #procedure = models.ManyToOneRel(PersonProcedure, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=_('name'))
    changes_state = models.BooleanField(default=False, verbose_name=_('changes status'), db_column='cambia_estado')
    changes_scholar_situation = models.BooleanField(default=False, verbose_name=_('changes scholar situation'), db_column='cambia_situacion_escolar')
    changes_structure = models.BooleanField(default=False, verbose_name=_('changes structure'), db_column='cambia_estructura')
    initials_procedure_states = models.ManyToManyField(ProcedureStateType,related_name='initials_procedure_states', verbose_name=_('initials procedure status'), db_column='estados_iniciales_tramite')
    final_procedure_state = models.ForeignKey(ProcedureStateType, on_delete=models.CASCADE, verbose_name=_('final procedure status'), db_column='estado_final_tramite')

    class Meta:
        verbose_name = _('Procedure Configuration')
        verbose_name_plural = _('Procedure Configurations')
        db_table = f'{APP_LABEL.lower()}_tbr_configuracion_tramite'
    
    def __str__(self):
        return self.name