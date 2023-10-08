from core.utils import APP_LABEL
from django.utils.translation import gettext_lazy as _

from .mdl_base_type import BaseType


class WorkerIncomeType(BaseType):
    
    """
        Used it on Procedure app
    """
    
    class Meta:
        verbose_name = _('Worker income type')
        verbose_name_plural = _('Worker income types')
        db_table = f'{APP_LABEL.lower()}_tbn_tipo_alta_trabajador'