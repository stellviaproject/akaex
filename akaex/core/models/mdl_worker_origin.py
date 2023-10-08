from core.utils import APP_LABEL
from django.utils.translation import gettext_lazy as _

from .mdl_base_type import BaseType


class WorkerOriginType(BaseType):
    
    """
        Used it on Procedure app
    """
    
    class Meta:
        verbose_name = _('Worker origin')
        verbose_name_plural = _('Worker origins')
        db_table = f'{APP_LABEL.lower()}_tbn_origen_trabajador'