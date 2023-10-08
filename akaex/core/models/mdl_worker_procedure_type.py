from core.utils import APP_LABEL
from django.utils.translation import gettext_lazy as _
from procedure import nom_types
from .mdl_base_type import BaseType
from django.db import models


class WorkerProcedureType(BaseType):
    
    """
        Used it on Procedure app
    """
    type = models.CharField(
                        max_length=100, choices=nom_types.WORKER_PROCEDURE_TYPE, 
                        default=nom_types.CONST_PROCEDURE_NONE, verbose_name=_('type'), 
                        db_column='tipo', unique=True)
    
    class Meta:
        verbose_name = _('Worker procedure type')
        verbose_name_plural = _('Worker procedure types')
        db_table = f'{APP_LABEL.lower()}_tbn_tipo_tramite_trabajador'