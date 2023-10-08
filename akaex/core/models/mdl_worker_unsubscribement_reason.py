from core.utils import APP_LABEL
from django.db import models
from django.utils.translation import gettext_lazy as _

from .mdl_base_type import BaseType


class WorkerUnsubscribementReasonType(BaseType):
    
    """
        Used it on Procedure app
        List the reasons why a worker can be terminated permanently
    """
    does_return = models.BooleanField()
    
    class Meta:
        verbose_name = _('Worker unsubscribement reason')
        verbose_name_plural = _('Worker unsubscribement reasons')
        db_table = f'{APP_LABEL.lower()}_tbn_motivo_baja_trabajador'
